
import pytest

from palindrome import is_palindrome


def test_non_string_input_raise_value_error():
    with pytest.raises(ValueError):
        is_palindrome(123)


def test_empty_string_returns_false():
    assert is_palindrome("") is False


def test_single_character_returns_true():
    assert is_palindrome("a") is True


def test_two_identical_characters_returns_true():
    assert is_palindrome("bb") is True


def test_non_palindrome_returns_false():
    assert is_palindrome("abc") is False

def test_laval_returna_true():
    assert is_palindrome("laval") is True

def test_toronto_returns_false():
    assert is_palindrome("toronto") is False

def test_sentence_palindrome_returns_true():
    assert is_palindrome("Able was I ere I saw Elba") is True
