import unittest
from .. import english_to_french, french_to_english

class TestTranslator(unittest.TestCase):
    def test_en_to_fr(self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour')

    def test_fr_to_en(self):
        self.assertEqual(french_to_english('Bonjour'), 'Hello')

if __name__ == "__main__":
    unittest.main()