# Migration Plan - Ingesting Notes and PYQs with Unified Resource Structure

## Problem Statement
Extend the uniAI-MCP system to serve notes and PYQs alongside syllabi. Restructure the entire resource organization to a unified hierarchy (`resources/AKTU/{year}/{subject_code}/{type}/...`) while maintaining the existing SQLite-based approach. Keep code changes minimal and consistent with current implementation style.

## Requirements
Based on project discussion (2026-10-17):

1. **Unified folder structure**: `resources/AKTU/{year}/{subject_code}/{type}/...`
   - Syllabus: `resources/AKTU/3/BCS501H/syllabus/aktu.md`
   - Notes: `resources/AKTU/3/BCS501H/notes/unit1/gateway-classes.md` (units 1-5)
   - PYQs: `resources/AKTU/3/BCS501H/pyq/2026-0.md` (indexed when multiple for same year)

2. **Subject scope**: All current files are for Database Management System (BCS501H), year 3

3. **Sources**: 
   - Syllabus: "AKTU"
   - Notes (all 5 units): "Gateway Classes"
   - PYQs: "AKTU"

4. **Naming conventions**:
   - Use subject codes (e.g., BCS501H) internally for uniqueness
   - Kebab-case for filenames (e.g., `gateway-classes.md`, `aktu.md`)
   - PYQ indexing: `2026-0.md`, `2026-1.md` when multiple papers for same year
   - Ensure disk structure matches database references

5. **Migration**: Move existing syllabus files to new structure

6. **Code style**: Minimal changes, match existing implementation patterns

7. **No RAG**: Direct file serving only

## Background

### Current Implementation Analysis
- Database schema already supports the resource types via `resource_type` enum: `'syllabus'`, `'notes'`, `'pyq'`
- Schema supports unit/label differentiation via `label` field (e.g., 'Unit 1', 'Unit 2')
- Current code in `utils.py` has helper functions: `get_syllabus_path()`, `load_syllabus()`
- Environment variables define root paths: `SYLLABUS_ROOT`, `NOTES_ROOT`, `PYQ_ROOT` (currently unused)
- Migration script pattern established in `ingest/migrate_syllabus_all.py`

### Extracted Files in `extract/to/`
- Notes: `unit1.md`, `unit2.md`, `unit3.md`, `unit4.md`, `unit5.md`
- PYQs: Multiple files like `01-2026.md`, `08-2025-2.md`, `19-2020.md`, etc. (need year extraction and indexing)

## Proposed Solution

### High-level Approach

1. **Restructure filesystem**: Create new unified folder hierarchy and migrate all content
2. **Normalize filenames**: Rename files to kebab-case and consistent naming
3. **Update environment variables**: Change to single `RESOURCES_ROOT` instead of separate type roots
4. **Extend database helpers**: Add `get_notes_path()`, `get_pyq_paths()` functions following existing pattern
5. **Implement MCP tools**: Complete `get_notes()`, add `get_pyq()` tool
6. **Create migration script**: Single script to ingest all content types with proper source attribution
7. **Update availability query**: Extend to show which resource types are available per subject

## Task Breakdown

### Task 1: Restructure Filesystem and Normalize Filenames

**Objective**: Create the new unified directory structure and move all content to proper locations with kebab-case naming.

**Implementation**:
- Create the new directory structure: `resources/AKTU/3/BCS501H/{syllabus,notes,pyq}/`
- Create unit subdirectories for notes: `notes/unit1/` through `notes/unit5/`
- Move and rename syllabus files from old structure to `resources/AKTU/3/BCS501H/syllabus/aktu.md`
- Copy and rename notes from `extract/to/unit{N}.md` to `resources/AKTU/3/BCS501H/notes/unit{N}/gateway-classes.md`
- Parse PYQ filenames, extract years, detect duplicates, and copy to `resources/AKTU/3/BCS501H/pyq/{year}-{index}.md`
- Ensure all filenames use kebab-case consistently

**Test**: Verify all files are in correct locations with correct naming

**Demo**: New directory structure is in place with all content properly organized

---

### Task 2: Update Environment Configuration and Database Schema Verification

**Objective**: Simplify environment configuration to use unified resource root.

**Implementation**:
- Update `.env` to use single `RESOURCES_ROOT` variable pointing to `resources/`
- Keep university name and year as separate config or hardcoded constants
- Verify database schema supports the new structure (it already does)
- Document the path convention: `{RESOURCES_ROOT}/{university}/{year}/{subject_code}/{type}/...`

**Test**: Load environment variables and verify paths resolve correctly

**Demo**: Configuration cleanly points to unified resource structure

---

### Task 3: Extend Database Utility Functions

**Objective**: Add helper functions for notes and PYQs following the existing pattern.

**Implementation**:
- Add `get_notes_path(code: str, unit: int) -> Path | None` that queries resources table with filters: `resource_type='notes'` and `label=f'Unit {unit}'`
- Add `get_pyq_paths(code: str) -> list[tuple[Path, str]]` that returns all PYQ paths with their labels (year-index)
- Update `get_syllabus_path()` to work with new structure (same query logic, just path construction changes)
- Update `load_syllabus()` to generic `load_resource(path: Path) -> str` if beneficial, or keep separate
- Update `RESOURCES_ROOT` import and path construction logic

**Test**: Call each function with test subject code and verify correct paths returned

**Demo**: Utility functions correctly resolve paths for all three resource types

---

### Task 4: Implement MCP Tool Functions

**Objective**: Complete the MCP tools to serve notes and PYQs.

**Implementation**:
- Complete the `get_notes(code: str, unit: int) -> str` tool implementation
  - Validate unit is 1-5
  - Call `get_notes_path()`, handle missing files gracefully
  - Load and return content
- Implement `get_pyq(code: str) -> str` tool
  - Call `get_pyq_paths()` to get all PYQs for subject
  - Format response to list available years/variants and return all content or structured listing
  - Handle missing PYQs gracefully
- Update `get_syllabus()` to work with new path structure

**Test**: Call each tool with valid/invalid inputs, verify error handling

**Demo**: All three MCP tools return correct content or appropriate error messages

---

### Task 5: Extend Availability Query to Show Resource Coverage

**Objective**: Make it clear which resource types are available for each subject.

**Implementation**:
- Modify `query_subject_all()` to include resource type availability per subject
- Query should return which resource types are available: `{code, name, has_syllabus, has_notes, has_pyq}`
- Or return structure: `{year, subjects: [{code, name, resources: ['syllabus', 'notes', 'pyq']}]}`
- Update `get_availability()` tool output format

**Test**: Call `get_availability()` and verify it shows resource type coverage

**Demo**: Availability tool clearly indicates which subjects have which resource types

---

### Task 6: Create Unified Migration/Ingestion Script

**Objective**: Single script to populate database with all resource mappings.

**Implementation**:
- Create `ingest/migrate_all_resources.py` script
- Insert or verify all sources: "AKTU", "Gateway Classes"
- Insert or verify subject: Database Management System (BCS501H), year 3
- Insert syllabus resource record with correct `file_path` relative to `RESOURCES_ROOT`
- Insert 5 notes resource records (Unit 1 through Unit 5) with source "Gateway Classes"
- Parse PYQ files, insert resource records with appropriate labels (year-index)
- Ensure `file_path` in database matches actual disk structure
- Print summary of what was inserted

**Test**: Run migration script, verify database records created correctly

**Demo**: Database populated with all resource mappings, paths match disk structure

---

### Task 7: Update MCP Prompt and Verification

**Objective**: Complete end-to-end testing and update user-facing documentation.

**Implementation**:
- Update `uniAI_instructions()` prompt to mention notes and PYQs
- Clarify that notes are unit-wise (1-5), PYQs are subject-wise by year
- Run the MCP server and test all tools end-to-end
- Test with valid subject codes and various units/years
- Test error cases (invalid codes, missing units, etc.)

**Test**: Start server, invoke all tools, verify responses

**Demo**: Complete working system serving syllabi, notes, and PYQs through MCP tools

---

## Success Criteria

- [ ] All content properly organized in unified directory structure
- [ ] Database correctly maps all resources to disk locations
- [ ] All three MCP tools (`get_syllabus`, `get_notes`, `get_pyq`) functional
- [ ] Availability tool shows accurate resource coverage
- [ ] No code bloat - minimal changes following existing patterns
- [ ] Consistent kebab-case naming throughout

## Notes

- Keep implementation minimal and consistent with existing style
- No RAG implementation in this phase
- Focus on Database Management System (BCS501H) initially
- Can be extended to other subjects following same pattern
