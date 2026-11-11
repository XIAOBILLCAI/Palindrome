
import pytest

from palindrome import is_palindrome


def test_onn_string_input_raise_value_error():
    with pytest.raises(ValueError):
        is_palindrome(123)
        
