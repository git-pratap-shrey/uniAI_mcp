import os
from pathlib import Path
from dotenv import load_dotenv
import sqlite3

load_dotenv()
DB_PATH = Path(os.environ["DB_PATH"])

connection = sqlite3.connect(DB_PATH)
cursor = connection.cursor()

# (name, code, year, filename)
SUBJECTS = [
    ("Database Management System",             "BCS501H",  3, "Database Management System.md"),
    ("Database Management Systems Lab",        "BCS551H",  3, "Database Management Systems Lab.md"),
    ("Design and Analysis of Algorithm",       "BCS503H",  3, "Design and Analysis of Algorithm.md"),
    ("Design and Analysis of Algorithm Lab",   "BCS553H",  3, "Design and Analysis of Algorithm Lab.md"),
    ("Machine Learning Techniques",            "BCS055H",  3, "Machine Learning Techniques.md"),
    ("Object Oriented System Design with C++", "BCS054H",  3, "Object Oriented System Design with C++.md"),
    ("Web Technology",                         "BCS502IH", 3, "Web Technology.md"),
    ("Web Technology Lab",                     "BCS552H",  3, "Web Technology Lab.md"),
]

# Ensure source exists
cursor.execute("INSERT OR IGNORE INTO sources (name) VALUES ('AKTU')")
cursor.execute("SELECT id FROM sources WHERE name = 'AKTU'")
source_id = cursor.fetchone()[0]

for name, code, year, filename in SUBJECTS:
    cursor.execute(
        "INSERT OR IGNORE INTO subjects (year, name, code) VALUES (?, ?, ?)",
        (year, name, code),
    )
    cursor.execute("SELECT id FROM subjects WHERE code = ?", (code,))
    subject_id = cursor.fetchone()[0]

    file_path = str(Path(str(year)) / filename)  # relative to SYLLABUS_ROOT
    cursor.execute(
        """INSERT OR IGNORE INTO resources (subject_id, resource_type, source_id, label, file_path)
           VALUES (?, 'syllabus', ?, '', ?)""",
        (subject_id, source_id, file_path),
    )
    print(f"  inserted: {name} ({code})")

connection.commit()
connection.close()
print("Migration complete.")
