# Developer Notes

## Quick Commands

- **Run inspector**: `npx @modelcontextprotocol/inspector@latest` (add custom streamable HTTP server `http://localhost:3001` directly)
- **Run project**: `uv run -m src.uniai_mcp.main` (or `uv run uniai-mcp`)
- **Run tunnel**: `cloudflared tunnel run projects`
- **Run tests**: `uv run pytest`
- **Run migrations**:
  - All resources (BCS501H syllabus, notes, pyq): `uv run python ingest/migrate_all_resources.py`
  - Syllabi migration: `uv run python ingest/add_missing_syllabi.py`
- **Run OCR extraction**:
  - Ollama async submit: `uv run python extract/extract_ollama.py`
  - Poll results: `uv run python extract/poll_results.py` (or `--once` for single sweep)

---

## Roadmap & Status

- [x] add syllabus migration script
- [x] add unified resource structure (`resources/AKTU/{year}/{code}/...`)
- [x] add pyq support (`get_pyq()`)
- [x] add notes support (`get_notes()` units 1–5)
- [x] add availability coverage check (`get_availability()`)
- [x] add pytest test suite (`test/`)
- [ ] add rag tools for notes;
- [ ] maybe enforce 1 syllabus per subject (later);
- [ ] add notes and pyqs for remaining Year 3 subjects;

---

*(Lab subjects won't have notes or PYQs, but still okay to keep syllabus if a user is just looking for it; the LLM can answer from the web if it has the syllabus.)*