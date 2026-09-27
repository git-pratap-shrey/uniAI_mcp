# Database Design and Architecture

## Overview
The migration from static availability JSON to SQLite aims to improve query efficiency, simplify tool interfaces, and entirely eliminate the need for fuzzy logic when resolving user requests. By utilizing the `code` as the definitive identifier, the LLM can precisely request resources after fetching the availability map.

## Schema Structure
Based on `db.sql`, the database employs three primary tables:

1. **`subjects` Table**
   - **Role:** Maps academic context (`year`) to specific subjects. Cross-semester subjects are consolidated under the year.
   - **Fields:** `id`, `year`, `name`, `code`.
   - **Constraints:** `UNIQUE(code)` enforces that subject codes are globally unique. `UNIQUE(year, name)` ensures no duplicate subjects per year.
   - **Indexes:** Lookups optimized by `idx_subjects_lookup` on `(year)`.

2. **`sources` Table**
   - **Role:** Centralizes names of resource origins (e.g., "Handwritten", "Source XYZ").
   - **Fields:** `id`, `name`.

3. **`resources` Table**
   - **Role:** Maps available materials to a given subject.
   - **Resource Types:** Constrained to `syllabus`, `notes`, `pyq`.
   - **Fields:** `id`, `subject_id`, `resource_type`, `source_id`, `label`, `file_path`.
   - **Relationships:** Links to `subjects` and `sources`.
   - **Constraints:** `UNIQUE(subject_id, resource_type, source_id, label)` allows multiple files for a given resource type (e.g., unit-wise breakdowns or multiple authors) without ambiguity.

## Tool Interface Mapping
The tools will enforce a deterministic, two-step lookup process:

1. **`get_availability()`**
   - **Action:** Queries the `subjects` table.
   - **Returns:** An aggregation of all available subjects, likely grouped by `year` (e.g., `[ { year: 1, subjects: [...] }, ... ]`).
   - **Purpose:** Informs the agent of the exact valid `code` mappings across the entire dataset at once.

2. **`get_syllabus(code)`** *(also applies to `get_notes`, `get_pyq`)*
   - **Action:** Performs an exact match using a SQL join:
     ```sql
     SELECT src.name AS source_name, r.label, r.file_path 
     FROM resources r 
     JOIN subjects s ON r.subject_id = s.id 
     JOIN sources src ON r.source_id = src.id
     WHERE s.code = ? AND r.resource_type = 'syllabus'
     ```
   - **Returns:** An array of results (containing `file_path`, `source_name`, and `label`) for the requested resource type.
   - **Purpose:** Provides 100% deterministic retrieval with no fuzzy string matching required. Supports fetching all chunks/units or alternative versions of a resource via the single `code` parameter.

## Design Questions & Considerations
*(See conversational output for ongoing design clarifications)*
