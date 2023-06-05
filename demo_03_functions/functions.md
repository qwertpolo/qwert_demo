# Najważniejsze funkcje pytest

Subiektywny wybór najważniejszych funkcji biblioteki pytest.

- [Najważniejsze funkcje pytest](#najważniejsze-funkcje-pytest)
  - [Treść](#treść)
    - [`pytest.main`](#pytestmain)
    - [`pytest.exit`](#pytestexit)
    - [`pytest.raises`](#pytestraises)
    - [`pytest.warns`](#pytestwarns)
    - [`pytest.fail`](#pytestfail)
    - [`pytest.approx`](#pytestapprox)

## Treść

### `pytest.main`

Rozpoczyna procedurę testową poprzez interpreter Pythona. W przeciwieństwie do pozostałych funkcji modułu, używana ona jest w skrypcie Pythona, a nie Ten sam efekt można użyskać poleceniem terminalu `pytest`.

### `pytest.exit`

Przerywa procedurę testową.

### `pytest.raises`

Sprawdza, czy test zgłasza błąd.

### `pytest.warns`

Sprzwdza czy test zgłasza ostrzeżenie.

### `pytest.fail`

Powoduje, że test nie przechodzi.

### `pytest.approx`

Sprawdza czy dwie wartości są w przybliżeniu równe.
