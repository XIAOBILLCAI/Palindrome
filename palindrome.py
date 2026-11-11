
from collections import deque

def is_palindrome(value):
    if not isinstance(value,str):
        raise ValueError("Input must be a string")

    if value == "":
        return False

    if len(value) == 1:
        return True

    #letters = deque(value)
    normalized = value.replace("","").lower()
    letters = deque(normalized)


    while len(letters) > 1:
        left = letters.popleft()
        right = letters.pop()

        if left != right:
            return False

    return True
