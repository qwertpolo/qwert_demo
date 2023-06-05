import pytest

div = (
    lambda a, b: a / b,
    lambda a, b: a / b if b else a,
)


@pytest.fixture(params=(0, 1))
def i(request):
    return request.param

# @pytest.mark.parametrize("i", [0, 1])
def test_div(i):
    with pytest.raises(ZeroDivisionError):
        div[i](1, 0)


if __name__ == "__main__":
    pytest.main([__file__])
