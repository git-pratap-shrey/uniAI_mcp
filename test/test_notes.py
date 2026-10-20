# Run command: uv run pytest test/test_notes.py
import json
import os
from pathlib import Path

import pytest

from uniai_mcp.main import get_availability, get_notes

RESOURCES_ROOT = Path(os.environ["RESOURCES_ROOT"])


def _note_cases():
    data = json.loads(get_availability())
    cases = []
    for year in data:
        for subject in year["subjects"]:
            code = subject["code"]
            if "notes" in subject["resources"]:
                for unit in range(1, 6):
                    cases.append((code, unit, True))
            else:
                cases.append((code, 1, False))
    return cases


def _note_files(code, unit):
    return sorted(RESOURCES_ROOT.glob(f"*/*/{code}/notes/unit{unit}/*.md"))


@pytest.mark.parametrize("code,unit,has_notes", _note_cases())
def test_notes_cross_verify(code, unit, has_notes):
    result = get_notes(code, unit)
    if has_notes:
        files = _note_files(code, unit)
        assert files, f"no notes file on disk for {code} unit {unit}"
        expected = files[0].read_text(encoding="utf-8")
        assert not result.startswith("ERROR")
        assert result == expected
    else:
        assert result.startswith("ERROR")


def test_notes_invalid_unit():
    assert get_notes("BCS501H", 0).startswith("ERROR")
    assert get_notes("BCS501H", 6).startswith("ERROR")
