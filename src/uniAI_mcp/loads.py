from pathlib import Path

SYLLABUS_ROOT = Path("resources/syllabus")

def get_syllabus_path(university: str, year: int, subject: str) -> Path:
    return SYLLABUS_ROOT / university / str(year) / f"{subject}.md"

def load_syllabus(university: str, year: int, subject: str) -> str:
    path = get_syllabus_path(university, year, subject)
    return path.read_text(encoding="utf-8")