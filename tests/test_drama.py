from unittest import TestCase

from livrel.constant import Metres, StageDirectionTypology
from livrel.drama import Verse


class TestVerse(TestCase):

    def test_verse_id(self):
        a = Verse(1, 'Hello World!', Metres.ALEXANDRIN)
        result = 1
        self.assertEqual(a.id_, result)

    def test_verse_text(self):
        a = Verse(1, 'Hello World!', Metres.ALEXANDRIN)
        result = 'Hello World!'
        self.assertEqual(a.text, result)

    def test_verse_metre(self):
        a = Verse(1, 'Hello World!', Metres.ALEXANDRIN)
        result = Metres.ALEXANDRIN
        self.assertEqual(a.metre, result)

    def test_verse_eq(self):
        a = Verse(1, 'Hello World!', Metres.ALEXANDRIN)
        b = Verse(1, 'Hello World!', Metres.DODECASYLLABE)
        self.assertEqual(a, b)

    def test_verse_dict(self):
        a = Verse(1, 'Hello World!', Metres.ALEXANDRIN)
        result = {'id_': 1, 'text': 'Hello World!', 'metre': 12}
        self.assertEqual(a.to_dict(), result)

    def test_verse_wrong_type_id(self):
        with self.assertRaises(ValueError):
            Verse('1', 'Hello World!', Metres.ALEXANDRIN)

    def test_verse_wrong_type_text(self):
        with self.assertRaises(ValueError):
            Verse(1, 2, Metres.ALEXANDRIN)

    def test_verse_wrong_type_metre(self):
        with self.assertRaises(ValueError):
            Verse(1, 'Hello World!', 12)