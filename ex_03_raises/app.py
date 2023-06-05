import pytest


def add(a, b):
    return a + b


def test_add():
    with pytest.raises(TypeError):
        add(3, "3")


if __name__ == "__main__":
    pytest.main([__file__])
