import pytest
from app import count_words

def test_count_words():
    """Testy w pytest nie wymagają deklaracji klas..."""
    assert count_words("") == 0
    assert count_words("Egg") == 1
    assert count_words("Egg ham") == 2
    assert count_words("Egg ham spam") == 3
    
