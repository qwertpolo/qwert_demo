import requests, pytest
from types import SimpleNamespace
from app import is_unicode


@pytest.fixture
def ok():
    def utf_8(*_, **__):
        return SimpleNamespace(encoding="utf-8")

    return utf_8


@pytest.fixture
def not_ok():
    def utf_16(*_, **__):
        return SimpleNamespace(encoding="utf-16")

    return utf_16


def test_is_unicode_utf_8(ok):
    requests.get = ok
    assert is_unicode("url", ("user", "pass")) == True


def test_is_unicode_utf_16(not_ok):
    requests.get = not_ok
    assert is_unicode("url", ("user", "pass")) == False


def test_is_unicode_error(ok):
    requests.get = ok
    with pytest.raises(TypeError):
        is_unicode("url")
