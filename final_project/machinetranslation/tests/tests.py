import sys
from pathlib import Path

if __name__ == '__main__' and __package__ is None:
    file = Path(__file__).resolve()
    parent, top = file.parent, file.parents[2]

    sys.path.append(str(top))
    try:
        sys.path.remove(str(parent))
    except ValueError: # Already removed
        pass

    import machinetranslation.tests
    __package__ = 'machinetranslation.tests'

import unittest
from ..translator import english_to_french, french_to_english

class TestTranslator(unittest.TestCase):
    def test_en_to_fr(self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
        self.assertNotEqual(english_to_french('Good Bye'), 'Bonjour')

    def test_fr_to_en(self):
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
        self.assertNotEqual(french_to_english('Bonjour'), 'Good Bye')

if __name__ == "__main__":
    unittest.main()