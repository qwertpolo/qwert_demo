import requests
from types import SimpleNamespace
from app import get_json


def test_get_json():
    """Test replaces get method in request via assignment and SimpleNamespace"""
    mock_response = SimpleNamespace(json=lambda *_: {"key": "value"})
    requests.get = lambda *_: mock_response
    assert get_json("url")["key"] == "value"
