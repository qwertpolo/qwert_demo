import datetime, app, pytest
from typing import Any


class MockNow:
    def __init__(self, h):
        self.hour = h

    def __call__(self) -> Any:
        return self


class MockDate:
    def __init__(self, h):
        self.now = MockNow(h)


def test_rand(monkeypatch):
    monkeypatch.setattr(datetime, "datetime", MockDate(8))
    s = app.is_day_or_night()
    s == "Dzień"
