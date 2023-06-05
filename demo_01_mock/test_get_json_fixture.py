import requests, pytest
from types import SimpleNamespace
from app import get_json

@pytest.fixture
def fix():
    return lambda *_: SimpleNamespace(json=lambda *_: {"key": "value"})


def test_get_json(fix):
    """Test replaces get method in request via assignment and SimpleNamespace"""
    requests.get = fix
    assert get_json("url")["key"] == "value"
