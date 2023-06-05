import unittest
from app import count_words

class TestCountWords(unittest.TestCase):
    def test_count(self):
        self.assertEqual(count_words(""), 0)
        self.assertEqual(count_words("Egg"), 1)
        self.assertEqual(count_words("Egg ham"), 2)
        self.assertEqual(count_words("Egg ham spam"), 3)

if __name__ == '__main__': unittest.main()