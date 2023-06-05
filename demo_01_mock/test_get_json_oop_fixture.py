import pytest, requests
from app import get_json


class MockResponse:
    @staticmethod
    def json():
        """Returns dictionary as a mock json response"""
        return {"key": "value"}


def test_get_json(monkeypatch):
    """Test replaces get method in request via monkeypatch and class declaration"""
    monkeypatch.setattr(requests, "get", lambda *_: MockResponse())
    assert get_json("url")["key"] == "value"
