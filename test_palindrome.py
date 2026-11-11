
import pytest

from palindrome import is_palindrome


def test_non_string_input_raise_value_error():
    with pytest.raises(ValueError):
        is_palindrome(123)


def test_empty_string_returns_false():
    assert is_palindrome("") is False
