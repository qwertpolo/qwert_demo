import pytest
from app import count_words

class TestCountWords:
    """...ale możemy zgrupować testy w klasę jeżeli zajdzie taka potrzeba."""
    def test_count(self):
        assert count_words("") == 0
        assert count_words("Egg") == 1
        assert count_words("Egg ham") == 2
        assert count_words("Egg ham spam") == 3
    def test_default(self):
        assert count_words() == 0
