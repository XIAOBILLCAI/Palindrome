import unittest

from palindrome import is_palindrome


class TestPalindrome(unittest.TestCase):

    def test_palindrome_word(self):
        self.assertTrue(is_palindrome("laval"))

    def test_non_palindrome_word(self):
        self.assertFalse(is_palindrome("toronto"))

    def test_sentence_palindrome(self):
        self.assertTrue(is_palindrome("Able was I ere I saw Elba"))

    def test_empty_string(self):
        self.assertFalse(is_palindrome(""))

    def test_non_string_input(self):
        with self.assertRaises(ValueError):
            is_palindrome(123)
