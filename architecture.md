# uniAI-MCP Architecture

## System Overview

**Purpose**: Model Context Protocol (MCP) server that provides AI agents with direct access to university study materials including syllabi, notes, and previous year questions (PYQs).

**Core Principles**:
- Database-driven resource mapping (no fuzzy matching or text search)
- Direct file serving (no RAG, no embeddings)
- Clean SQLite database for reliable subject-to-resource mapping
- Minimal code, consistent patterns
- Extensible to multiple universities, years, and subjects

## Directory Structure

### Unified Resource Hierarchy

```
resources/
  {university}/              # e.g., "AKTU"
    {year}/                  # e.g., "3" (3rd year)
      {subject_code}/        # e.g., "BCS501H"
        syllabus/            # Single syllabus file per source
          {source}.md        # e.g., "aktu.md"
        notes/               # Unit-wise organization (1-5)
          unit1/
            {source}.md      # e.g., "gateway-classes.md"
          unit2/
            {source}.md
          unit3/
            {source}.md
          unit4/
            {source}.md
          unit5/
            {source}.md
        pyq/                 # Previous year questions
          {year}-{index}.md  # e.g., "2026-0.md", "2025-0.md", "2025-1.md"
```

### Other Directories

```
src/uniai_mcp/        # Main application code
  main.py             # MCP server and tool definitions
  utils.py            # Database queries and file loading utilities

ingest/               # Migration and data ingestion scripts
  migrate_*.py        # Scripts to populate database

extract/              # Temporary extraction area for PDF processing
  to/                 # Extracted markdown files (not part of resources)

test/                 # Comprehensive pytest test suites
  test_*.py           # Verification tests for availability, syllabus, notes, pyqs
  conftest.py         # Pytest configuration and environment loading

database.db           # SQLite database
db.sql                # Database schema definition
.env                  # Environment configuration
```

## Naming Conventions

### Subject Identification
- **Always use subject codes** (e.g., `BCS501H`) for internal references and database queries
- Subject codes are unique across the system
- Avoid using subject names for lookups to prevent string mismatches

### File Naming
- **Kebab-case** for all filenames: `gateway-classes.md`, `aktu.md`
- Normalize spaces and special characters to hyphens
- Lowercase preferred

### PYQ Indexing
- Format: `{year}-{index}.md`
- Index is `0, 1, 2, ...` for multiple papers in the same year
- Examples: `2026-0.md`, `2025-0.md`, `2025-1.md`, `2024-0.md`

### Database-Disk Consistency
- The `file_path` field in the `resources` table must **exactly match** the actual disk path relative to `RESOURCES_ROOT`
- Example DB entry: `file_path = "AKTU/3/BCS501H/notes/unit1/gateway-classes.md"`
- Must resolve to: `{RESOURCES_ROOT}/AKTU/3/BCS501H/notes/unit1/gateway-classes.md`

## Database Schema

### Tables

#### `subjects`
Stores academic subjects with their codes and metadata.

```sql
CREATE TABLE subjects (
    id        INTEGER PRIMARY KEY,
    year      INTEGER NOT NULL,
    name      TEXT NOT NULL,
    code      TEXT NOT NULL,
    UNIQUE(code),
    UNIQUE(year, name)
);
```

**Fields**:
- `id`: Auto-incrementing primary key
- `year`: Academic year (e.g., 1, 2, 3, 4)
- `name`: Full subject name (e.g., "Database Management System")
- `code`: Unique subject code (e.g., "BCS501H")

#### `sources`
Tracks the source/origin of study materials.

```sql
CREATE TABLE sources (
    id    INTEGER PRIMARY KEY,
    name  TEXT NOT NULL UNIQUE
);
```

**Fields**:
- `id`: Auto-incrementing primary key
- `name`: Source name (e.g., "AKTU", "Gateway Classes", "Handwritten")

**Examples**:
- "AKTU" - Official university materials
- "Gateway Classes" - Notes from Gateway Classes coaching
- "MIT OCW" - Materials from MIT OpenCourseWare

#### `resources`
Maps subjects to their actual resource files on disk.

```sql
CREATE TABLE resources (
    id            INTEGER PRIMARY KEY,
    subject_id    INTEGER NOT NULL REFERENCES subjects(id),
    resource_type TEXT NOT NULL CHECK (resource_type IN ('syllabus','notes','pyq')),
    source_id     INTEGER NOT NULL REFERENCES sources(id),
    label         TEXT NOT NULL DEFAULT '',
    file_path     TEXT NOT NULL,
    UNIQUE(subject_id, resource_type, source_id, label)
);
```

**Fields**:
- `id`: Auto-incrementing primary key
- `subject_id`: Foreign key to `subjects` table
- `resource_type`: One of: `'syllabus'`, `'notes'`, `'pyq'`
- `source_id`: Foreign key to `sources` table
- `label`: Contextual label for the resource
  - For notes: `'Unit 1'`, `'Unit 2'`, ..., `'Unit 5'`
  - For PYQs: `'2026-0'`, `'2025-0'`, `'2025-1'`, etc.
  - For syllabus: Empty string `''`
- `file_path`: Path to file **relative to `RESOURCES_ROOT`**

**Example Records**:
```sql
-- Syllabus
(subject_id=1, resource_type='syllabus', source_id=1, label='', 
 file_path='AKTU/3/BCS501H/syllabus/aktu.md')

-- Notes
(subject_id=1, resource_type='notes', source_id=2, label='Unit 1',
 file_path='AKTU/3/BCS501H/notes/unit1/gateway-classes.md')

-- PYQ
(subject_id=1, resource_type='pyq', source_id=1, label='2026-0',
 file_path='AKTU/3/BCS501H/pyq/2026-0.md')
```

### Indexes

```sql
CREATE INDEX idx_subjects_lookup ON subjects(year);
```

## Code Architecture

### Configuration (`src/uniai_mcp/.env`)

```bash
BASE_DIR=/home/anon/PROJECTS/uniAI-MCP
DB_PATH=/home/anon/PROJECTS/uniAI-MCP/database.db
RESOURCES_ROOT=/home/anon/PROJECTS/uniAI-MCP/resources
```

**Environment Variables**:
- `BASE_DIR`: Project root directory
- `DB_PATH`: Path to SQLite database file
- `RESOURCES_ROOT`: Root directory for all study materials

### Utility Functions Pattern (`src/uniai_mcp/utils.py`)

All database query utilities follow the same pattern:

```python
def get_{type}_path(code: str, ...) -> Path | None:
    """
    Query database for resource file path.
    Returns Path object or None if not found.
    """
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()
    
    cursor.execute('''
        SELECT r.file_path 
        FROM resources r 
        JOIN subjects s ON r.subject_id = s.id 
        WHERE s.code = ? AND r.resource_type = ? AND [additional filters]
    ''', (code, type, ...))
    
    row = cursor.fetchone()
    connection.close()
    
    if not row:
        return None
    
    path_in_db = row[0]
    return RESOURCES_ROOT / path_in_db
```

**Implemented Functions**:
- `get_syllabus_path(code: str) -> Path | None`: Queries `resources` table for syllabus file path.
- `get_notes_path(code: str, unit: int) -> Path | None`: Queries `resources` table for unit notes file path (`label='Unit {unit}'`).
- `get_pyq_paths(code: str) -> list[tuple[Path, str]]`: Queries `resources` table for all PYQ files and their labels (`label` formatted as `{year}-{index}`).
- `load_resource(path: Path) -> str`: Generic file loader returning markdown contents encoded as UTF-8.
- `query_subject_all() -> list[dict[str, Any]]`: Returns all subjects grouped by academic year with available resource types array (`['syllabus', 'notes', 'pyq']`).

### MCP Tool Pattern (`src/uniai_mcp/main.py`)

All MCP tools follow this pattern:

```python
@mcp.tool()
def get_{type}(code: str, ...) -> str:
    """
    Fetch the {type} content for a subject. 
    Check the availability tool first.
    """
    path = get_{type}_path(code, ...)
    if not path or not path.exists():
        return f"ERROR: {Type} missing for subject code {code}."
    
    return path.read_text(encoding="utf-8")
```

**Implemented Tools**:
- `get_syllabus(code: str) -> str`: Fetches complete syllabus content for a subject code.
- `get_notes(code: str, unit: int) -> str`: Fetches notes for a specific unit (1-5) for a subject code.
- `get_pyq(code: str) -> str`: Fetches all previous year question papers for a subject code, formatted with clear year headers.
- `get_availability() -> str`: Lists all supported academic years, subjects, codes, and available resource types in JSON format.
- `uniAI_instructions()` (MCP Prompt): Provides instructions to LLMs on proper tool invocation sequence.

### Migration Script Pattern (`ingest/migrate_*.py`)

Standard pattern for database population:

```python
import os
from pathlib import Path
from dotenv import load_dotenv
import sqlite3

load_dotenv()
DB_PATH = Path(os.environ["DB_PATH"])

connection = sqlite3.connect(DB_PATH)
cursor = connection.cursor()

# 1. Ensure sources exist
cursor.execute("INSERT OR IGNORE INTO sources (name) VALUES (?)", (source_name,))
cursor.execute("SELECT id FROM sources WHERE name = ?", (source_name,))
source_id = cursor.fetchone()[0]

# 2. Insert subjects
cursor.execute(
    "INSERT OR IGNORE INTO subjects (year, name, code) VALUES (?, ?, ?)",
    (year, name, code),
)
cursor.execute("SELECT id FROM subjects WHERE code = ?", (code,))
subject_id = cursor.fetchone()[0]

# 3. Insert resources
file_path = str(Path(...))  # relative to RESOURCES_ROOT
cursor.execute(
    """INSERT OR IGNORE INTO resources 
       (subject_id, resource_type, source_id, label, file_path)
       VALUES (?, ?, ?, ?, ?)""",
    (subject_id, resource_type, source_id, label, file_path),
)

connection.commit()
connection.close()
```

## Current Implementation Status

### ✅ Implemented
- [x] SQLite database with `subjects`, `sources`, `resources` tables
- [x] Basic MCP server setup with streamable HTTP and transport security
- [x] Unified resource directory structure (`resources/{university}/{year}/{subject_code}/...`)
- [x] Syllabus serving functionality (`get_syllabus()` tool)
- [x] Unit-wise notes serving (`get_notes()` tool for units 1–5)
- [x] Previous year questions serving (`get_pyq()` tool with year labels)
- [x] Enhanced availability query and tool (`get_availability()`) showing resource type coverage
- [x] Initial subject ingestion (8 subjects, Year 3 AKTU) with unified syllabus hierarchy
- [x] BCS501H ingestion with 5 units of notes (Gateway Classes) and 34 PYQ papers (AKTU, 2016–2026)
- [x] Migration scripts (`migrate_all_resources.py`, `add_missing_syllabi.py`)
- [x] Comprehensive pytest test suites (`test/`) with cross-verification of database and disk files

### 🔄 In Progress
- [ ] Ingesting notes and PYQs for remaining Year 3 subjects (BCS502IH, BCS503H, BCS054H, BCS055H)
- [ ] RAG / semantic search tools for long-form notes (optional future addition)

### 📋 Future Enhancements
- [ ] Support multiple universities
- [ ] Support multiple years and semesters
- [ ] Support multiple sources per resource type
- [ ] Web interface for content browsing
- [ ] RAG/semantic search capabilities
- [ ] PDF upload and automatic extraction pipeline

## Design Decisions

### Why SQLite?
- Simple, zero-configuration database
- Perfect for single-server deployment
- Reliable ACID transactions
- No external database server required
- Easy to backup (single file)

### Why No Fuzzy Matching?
- Fuzzy matching is error-prone and unpredictable
- Subject codes provide unique, reliable identifiers
- Database lookups are fast and deterministic
- AI agents can easily query availability before access

### Why No RAG (for now)?
- Start simple: direct file serving meets immediate needs
- Avoids complexity of vector databases and embeddings
- Easy to add later if semantic search becomes necessary
- Current approach is fast and reliable

### Why Separate Sources?
- Acknowledge multiple content creators
- Allow students to prefer specific sources
- Support future features like source ratings or preferences
- Maintain proper attribution

### Why Unit-wise Notes?
- Aligns with how courses are structured
- Makes content more manageable and discoverable
- Allows selective studying by unit
- Natural chunking for future RAG implementation

## Extension Guidelines

### Adding a New Subject

1. Organize files in correct directory structure
2. Add subject to database via migration script:
   ```python
   cursor.execute(
       "INSERT OR IGNORE INTO subjects (year, name, code) VALUES (?, ?, ?)",
       (year, "Subject Name", "SUBJECT_CODE")
   )
   ```
3. Add resource mappings for syllabus, notes, PYQs as applicable
4. Verify with `get_availability()` tool

### Adding a New University

1. Create new university directory: `resources/{UNIVERSITY_NAME}/`
2. Follow same year/subject/type structure
3. Insert source record for university materials
4. Add subjects and resources following standard pattern
5. Update `get_availability()` to filter/group by university if needed

### Adding a New Resource Type

1. Update `resource_type` CHECK constraint in `db.sql`
2. Create utility function `get_{type}_path()` in `utils.py`
3. Create MCP tool `get_{type}()` in `main.py`
4. Update migration scripts to support new type
5. Update availability query to include new type

## Security Considerations

- MCP server uses `TransportSecuritySettings` with allowed hosts
- File access is restricted to paths within `RESOURCES_ROOT`
- Database queries use parameterized statements (SQL injection protection)
- No user-uploaded content (yet) - all content is admin-curated

## Performance Considerations

- SQLite is fast enough for expected load (small number of concurrent users)
- File I/O is direct (no caching layer yet)
- Markdown files are small enough to serve directly
- For future scaling: consider caching frequently accessed files in memory

## Troubleshooting

### Tool returns "ERROR: ... missing for subject code"
- Verify subject code is correct using `get_availability()`
- Check database has resource record for that subject/type
- Verify file exists at the path specified in database
- Check file permissions

### Database path issues
- Ensure `file_path` in database matches actual disk structure exactly
- Paths should be relative to `RESOURCES_ROOT`
- Use forward slashes even on Windows
- No leading slash in `file_path`

### Environment variables not loading
- Ensure `.env` file is in project root
- Check `load_dotenv()` is called before importing local modules
- Verify paths are absolute, not relative
