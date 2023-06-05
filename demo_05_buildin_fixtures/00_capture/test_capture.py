import pytest


# Fixtura capsys ma też alias capfd
def test_print(capsys):
    print("hi", end="")
    assert capsys.readouterr().out == "hi"


def test_print_2(capfd):
    print("yo", end="")
    assert capfd.readouterr().out == "yo"


if __name__ == "__main__":
    pytest.main([__file__])
