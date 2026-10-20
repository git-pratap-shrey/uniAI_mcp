# Run command: uv run pytest test/test_pyq.py
import json
import os
from pathlib import Path

import pytest

from uniai_mcp.main import get_availability, get_pyq

RESOURCES_ROOT = Path(os.environ["RESOURCES_ROOT"])


def _pyq_cases():
    data = json.loads(get_availability())
    cases = []
    for year in data:
        for subject in year["subjects"]:
            cases.append((subject["code"], "pyq" in subject["resources"]))
    return cases


def _pyq_expected(code):
    files = sorted(RESOURCES_ROOT.glob(f"*/*/{code}/pyq/*.md"))
    parts = []
    for f in files:
        label = f.stem
        parts.append(f"--- {label} ---\n{f.read_text(encoding='utf-8')}")
    return "\n\n".join(parts)


@pytest.mark.parametrize("code,has_pyq", _pyq_cases())
def test_pyq_cross_verify(code, has_pyq):
    result = get_pyq(code)
    if has_pyq:
        expected = _pyq_expected(code)
        assert expected, f"no pyq files on disk for {code}"
        assert not result.startswith("ERROR")
        assert result == expected
    else:
        assert result.startswith("ERROR")
