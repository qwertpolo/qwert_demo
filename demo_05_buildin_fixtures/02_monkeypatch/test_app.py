import requests
from app import get_json


class MockResponse:
    @staticmethod
    def json():
        return {"key": "value"}


def test_get_json(monkeypatch):
    monkeypatch.setattr(requests, "get", lambda *_: MockResponse())
    assert get_json("url")["key"] == "value"
