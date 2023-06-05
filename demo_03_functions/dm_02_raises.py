import pytest

div = (
    lambda a, b: a / b,
    lambda a, b: a / b if b else a,
)


def test_div_0(arg):
    with pytest.raises(ZeroDivisionError):
        div[0](1, 0)


def test_div_0(arg):
    with pytest.raises(ZeroDivisionError):
        div[1](1, 0)


if __name__ == "__main__":
    pytest.main([__file__])
