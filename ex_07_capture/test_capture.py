from app import reverse_print


def test_reverse_print_single_arg(capsys):
    reverse_print("Hello")
    assert capsys.readouterr().out == "olleH\n"


def test_reverse_print_multiple_args(capsys):
    reverse_print("Hello", "world")
    assert capsys.readouterr().out == "dlrow olleH\n"


def test_reverse_print_non_string(capsys):
    reverse_print(123, True)
    assert capsys.readouterr().out == "eurT 321\n"


def test_reverse_print_end(capsys):
    reverse_print("Hello", end="world")
    assert capsys.readouterr().out.endswith("world")


def test_reverse_print_end(capsys):
    reverse_print("Hello")
    assert capsys.readouterr().out.endswith("\n")