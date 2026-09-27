from pathlib import Path
from typing import Any
import sqlite3

SYLLABUS_ROOT = Path("resources/syllabus/AKTU")
# NOTES_ROOT = Path("resources/pyqs/AKTU")
# PYQ_ROOT = Path("resources/notes/AKTU")


def get_syllabus_path(code: str) -> Path:
    connection = sqlite3.connect("app.db")
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
        raise FileNotFoundError(f"No syllabus found for subject code: {code}")

    path_in_db = row[0]

    return SYLLABUS_ROOT / path_in_db

def load_syllabus(path: Path) -> str:
    return path.read_text(encoding="utf-8")

def query_subject_all() -> list[dict[str, Any]]:
    connection = sqlite3.connect("app.db")
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()

    cursor.execute('''
        SELECT year, code, name 
        FROM subjects 
        ORDER BY year, name
    ''')
    
    rows = cursor.fetchall()
    connection.close()

    grouped = {}
    for row in rows:
        year = row["year"]
        if year not in grouped:
            grouped[year] = []
        grouped[year].append({"code": row["code"], "name": row["name"]})

    # {year, subjects: [{code, name}]}
    return [{"year": y, "subjects": s} for y, s in grouped.items()]
