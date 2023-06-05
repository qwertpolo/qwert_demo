import random, pytest, app


@pytest.fixture
def fix():
    return lambda *_: 1


def test_rand(monkeypatch, capsys, fix):
    monkeypatch.setattr(random, "randint", fix)
    app.roll_3d6()
    capsys.readouterr().out == "1\n1\n1\n"
