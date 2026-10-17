import os
from pathlib import Path
from typing import Any
import sqlite3

BASE_DIR = Path(os.environ["BASE_DIR"])
DB_PATH = Path(os.environ["DB_PATH"])
RESOURCES_ROOT = Path(os.environ["RESOURCES_ROOT"])


def get_syllabus_path(code: str) -> Path | None:
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()

    cursor.execute('''
        SELECT r.file_path 
        FROM resources r 
        JOIN subjects s ON r.subject_id = s.id 
        WHERE s.code = ? AND r.resource_type = 'syllabus'
    ''', (code,))
    
    row = cursor.fetchone()
    connection.close()
    
    if not row:
        return None

    path_in_db = row[0]
    return RESOURCES_ROOT / path_in_db


def load_resource(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def get_notes_path(code: str, unit: int) -> Path | None:
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()

    cursor.execute('''
        SELECT r.file_path 
        FROM resources r 
        JOIN subjects s ON r.subject_id = s.id 
        WHERE s.code = ? AND r.resource_type = 'notes' AND r.label = ?
    ''', (code, f'Unit {unit}'))
    
    row = cursor.fetchone()
    connection.close()
    
    if not row:
        return None

    path_in_db = row[0]
    return RESOURCES_ROOT / path_in_db


def get_pyq_paths(code: str) -> list[tuple[Path, str]]:
    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()

    cursor.execute('''
        SELECT r.file_path, r.label
        FROM resources r 
        JOIN subjects s ON r.subject_id = s.id 
        WHERE s.code = ? AND r.resource_type = 'pyq'
        ORDER BY r.label
    ''', (code,))
    
    rows = cursor.fetchall()
    connection.close()
    
    if not rows:
        return []

    return [(RESOURCES_ROOT / row["file_path"], row["label"]) for row in rows]


def query_subject_all() -> list[dict[str, Any]]:
    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()

    cursor.execute('''
        SELECT year, code, name, 
               MAX(CASE WHEN r.resource_type = 'syllabus' THEN 1 ELSE 0 END) as has_syllabus,
               MAX(CASE WHEN r.resource_type = 'notes' THEN 1 ELSE 0 END) as has_notes,
               MAX(CASE WHEN r.resource_type = 'pyq' THEN 1 ELSE 0 END) as has_pyq
        FROM subjects s
        LEFT JOIN resources r ON s.id = r.subject_id
        GROUP BY s.id
        ORDER BY year, name
    ''')
    
    rows = cursor.fetchall()
    connection.close()

    grouped = {}
    for row in rows:
        year = row["year"]
        if year not in grouped:
            grouped[year] = []
        
        resources = []
        if row["has_syllabus"]:
            resources.append("syllabus")
        if row["has_notes"]:
            resources.append("notes")
        if row["has_pyq"]:
            resources.append("pyq")
        
        grouped[year].append({
            "code": row["code"], 
            "name": row["name"],
            "resources": resources
        })

    return [{"year": y, "subjects": s} for y, s in grouped.items()]
