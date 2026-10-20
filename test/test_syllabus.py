# Run command: uv run pytest test/test_syllabus.py
import json
import os
from pathlib import Path

import pytest

from uniai_mcp.main import get_availability, get_syllabus

RESOURCES_ROOT = Path(os.environ["RESOURCES_ROOT"])


def _subjects():
    data = json.loads(get_availability())
    return [(y, s) for y in data for s in y["subjects"]]


def _syllabus_files(code):
    return sorted(RESOURCES_ROOT.glob(f"*/*/{code}/syllabus/*.md"))


@pytest.mark.parametrize("year,subject", _subjects())
def test_syllabus_cross_verify(year, subject):
    code = subject["code"]
    result = get_syllabus(code)
    if "syllabus" in subject["resources"]:
        files = _syllabus_files(code)
        assert files, f"no syllabus file on disk for {code}"
        expected = files[0].read_text(encoding="utf-8")
        assert not result.startswith("ERROR")
        assert result == expected
    else:
        assert result.startswith("ERROR")


def test_syllabus_all_codes_from_availability():
    data = json.loads(get_availability())
    codes = [s["code"] for y in data for s in y["subjects"]]
    assert codes
    for code in codes:
        assert isinstance(get_syllabus(code), str)
