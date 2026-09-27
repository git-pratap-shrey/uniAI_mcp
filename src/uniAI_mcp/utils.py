import os
from pathlib import Path
from typing import Any
import sqlite3

BASE_DIR = Path(os.environ["BASE_DIR"])
DB_PATH = Path(os.environ["DB_PATH"])

SYLLABUS_ROOT = Path(os.environ["SYLLABUS_ROOT"])
# NOTES_ROOT = Path(os.environ["NOTES_ROOT"])
# PYQ_ROOT = Path(os.environ["PYQ_ROOT"])


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

    return SYLLABUS_ROOT / path_in_db

def load_syllabus(path: Path) -> str:
    return path.read_text(encoding="utf-8")

def query_subject_all() -> list[dict[str, Any]]:
    connection = sqlite3.connect(DB_PATH)
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
