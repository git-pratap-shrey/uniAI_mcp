# Run command: uv run python ingest/migrate_all_resources.py
import os
from pathlib import Path
from dotenv import load_dotenv
import sqlite3
import re

load_dotenv()
DB_PATH = Path(os.environ["DB_PATH"])
RESOURCES_ROOT = Path(os.environ["RESOURCES_ROOT"])
EXTRACT_DIR = Path("/home/anon/PROJECTS/uniAI-MCP/extract/to")

def extract_year(filename: str) -> str | None:
    """Extract year from PYQ filename like '01-2026.md' or '08-2025-2.md'."""
    match = re.search(r'-(\d{4})(?:-\w+)?\.md$', filename)
    if match:
        return match.group(1)
    return None

def main():
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()
    
    # Ensure sources exist
    cursor.execute("INSERT OR IGNORE INTO sources (name) VALUES (?)", ("AKTU",))
    cursor.execute("SELECT id FROM sources WHERE name = 'AKTU'")
    aktu_source_id = cursor.fetchone()[0]
    
    cursor.execute("INSERT OR IGNORE INTO sources (name) VALUES (?)", ("Gateway Classes",))
    cursor.execute("SELECT id FROM sources WHERE name = 'Gateway Classes'")
    gateway_source_id = cursor.fetchone()[0]
    
    # Get BCS501H subject
    cursor.execute("SELECT id FROM subjects WHERE code = ?", ("BCS501H",))
    row = cursor.fetchone()
    if not row:
        print("ERROR: Subject BCS501H not found in database")
        connection.close()
        return
    subject_id = row[0]
    
    # ===== 1. Move and rename syllabus files =====
    old_syllabus = RESOURCES_ROOT / "syllabus" / "AKTU" / "3" / "Database Management System.md"
    new_syllabus_dir = RESOURCES_ROOT / "AKTU" / "3" / "BCS501H" / "syllabus"
    new_syllabus_dir.mkdir(parents=True, exist_ok=True)
    new_syllabus = new_syllabus_dir / "aktu.md"
    
    if old_syllabus.exists():
        old_syllabus.rename(new_syllabus)
        print(f"Moved syllabus: {old_syllabus} -> {new_syllabus}")
    else:
        print(f"WARNING: Syllabus not found at {old_syllabus}")
    
    # Update syllabus resource record
    file_path = str(Path("AKTU") / "3" / "BCS501H" / "syllabus" / "aktu.md")
    cursor.execute(
        """UPDATE resources SET file_path = ? WHERE subject_id = ? AND resource_type = 'syllabus'""",
        (file_path, subject_id),
    )
    print(f"  updated syllabus: {file_path}")
    
    # ===== 2. Copy and rename notes (unit1.md through unit5.md) =====
    for unit_num in range(1, 6):
        old_notes = EXTRACT_DIR / f"unit{unit_num}.md"
        if old_notes.exists():
            notes_dir = RESOURCES_ROOT / "AKTU" / "3" / "BCS501H" / "notes" / f"unit{unit_num}"
            notes_dir.mkdir(parents=True, exist_ok=True)
            new_notes = notes_dir / "gateway-classes.md"
            old_notes.rename(new_notes)
            print(f"Moved notes (Unit {unit_num}): {old_notes} -> {new_notes}")
            
            # Insert notes resource
            file_path = str(Path("AKTU") / "3" / "BCS501H" / "notes" / f"unit{unit_num}" / "gateway-classes.md")
            cursor.execute(
                """INSERT OR IGNORE INTO resources (subject_id, resource_type, source_id, label, file_path)
                   VALUES (?, 'notes', ?, 'Unit ' || ?, ?)""",
                (subject_id, gateway_source_id, unit_num, file_path),
            )
            print(f"  inserted notes Unit {unit_num}")
        else:
            print(f"WARNING: Notes not found for Unit {unit_num}")
    
    # ===== 3. Process PYQ files =====
    # Group by year, then assign index
    pyq_files = {}
    for f in EXTRACT_DIR.glob("*.md"):
        if f.name.startswith("unit"):
            continue  # Skip notes files
        year = extract_year(f.name)
        if year:
            if year not in pyq_files:
                pyq_files[year] = []
            pyq_files[year].append(f)
    
    for year in sorted(pyq_files.keys()):
        files = pyq_files[year]
        # Sort files to ensure consistent indexing
        files.sort(key=lambda x: x.name)
        
        for idx, old_file in enumerate(files):
            pyq_dir = RESOURCES_ROOT / "AKTU" / "3" / "BCS501H" / "pyq"
            pyq_dir.mkdir(parents=True, exist_ok=True)
            new_pyq = pyq_dir / f"{year}-{idx}.md"
            old_file.rename(new_pyq)
            print(f"Moved PYQ ({year}-{idx}): {old_file} -> {new_pyq}")
            
            # Insert pyq resource
            file_path = str(Path("AKTU") / "3" / "BCS501H" / "pyq" / f"{year}-{idx}.md")
            label = f"{year}-{idx}"
            cursor.execute(
                """INSERT OR IGNORE INTO resources (subject_id, resource_type, source_id, label, file_path)
                   VALUES (?, 'pyq', ?, ?, ?)""",
                (subject_id, aktu_source_id, label, file_path),
            )
            print(f"  inserted pyq {year}-{idx}")
    
    connection.commit()
    connection.close()
    print("\nMigration complete.")

if __name__ == "__main__":
    main()
