# Run command: uv run pytest test/test_availability.py
import json

from uniai_mcp.main import get_availability


def test_get_availability_returns_list():
    data = json.loads(get_availability())
    assert isinstance(data, list)
    assert len(data) > 0


def test_get_availability_contains_subjects():
    data = json.loads(get_availability())
    codes = [s["code"] for year in data for s in year["subjects"]]
    assert len(codes) > 0
    assert "BCS501H" in codes


def test_get_availability_subjects_have_resources():
    data = json.loads(get_availability())
    for year in data:
        for subject in year["subjects"]:
            assert "code" in subject
            assert "name" in subject
            assert "resources" in subject
            assert isinstance(subject["resources"], list)
