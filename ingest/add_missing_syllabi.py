# Run command: uv run python ingest/add_missing_syllabi.py
import os
from pathlib import Path
from dotenv import load_dotenv
import sqlite3

load_dotenv()
DB_PATH = Path(os.environ["DB_PATH"])
RESOURCES_ROOT = Path(os.environ["RESOURCES_ROOT"])

# Subject mappings: (code, filename in resources/AKTU/3/{code}/syllabus/)
SUBJECTS = [
    ("BCS551H", "Database Management Systems Lab"),
    ("BCS503H", "Design and Analysis of Algorithm"),
    ("BCS553H", "Design and Analysis of Algorithm Lab"),
    ("BCS055H", "Machine Learning Techniques"),
    ("BCS054H", "Object Oriented System Design with C++"),
    ("BCS502IH", "Web Technology"),
    ("BCS552H", "Web Technology Lab"),
]

def main():
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()
    
    # Ensure source exists
    cursor.execute("INSERT OR IGNORE INTO sources (name) VALUES (?)", ("AKTU",))
    cursor.execute("SELECT id FROM sources WHERE name = 'AKTU'")
    source_id = cursor.fetchone()[0]
    
    for code, name in SUBJECTS:
        # Get subject id
        cursor.execute("SELECT id FROM subjects WHERE code = ?", (code,))
        row = cursor.fetchone()
        if not row:
            print(f"ERROR: Subject {code} not found")
            continue
        subject_id = row[0]
        
        # Create directory
        syllabus_dir = RESOURCES_ROOT / "AKTU" / "3" / code / "syllabus"
        syllabus_dir.mkdir(parents=True, exist_ok=True)
        
        # Copy from temp with new naming
        src = Path("/tmp") / f"{code}.md"
        dst = syllabus_dir / f"{code.lower()}.md"
        
        if src.exists():
            content = src.read_text()
            dst.write_text(content, encoding="utf-8")
            print(f"Copied: {src} -> {dst}")
            
            # Update database
            file_path = str(Path("AKTU") / "3" / code / "syllabus" / f"{code.lower()}.md")
            cursor.execute(
                """UPDATE resources SET file_path = ? WHERE subject_id = ? AND resource_type = 'syllabus'""",
                (file_path, subject_id),
            )
            print(f"  Updated DB: {file_path}")
        else:
            print(f"ERROR: Source file not found: {src}")
    
    connection.commit()
    connection.close()
    print("\nSyllabi migration complete.")

if __name__ == "__main__":
    main()
