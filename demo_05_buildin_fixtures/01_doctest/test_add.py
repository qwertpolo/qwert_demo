import pytest
import app

@pytest.fixture(autouse=True)
def doctest_add(doctest_namespace):
    doctest_namespace["add"] = app


# to run test: pytest --doctest-modules