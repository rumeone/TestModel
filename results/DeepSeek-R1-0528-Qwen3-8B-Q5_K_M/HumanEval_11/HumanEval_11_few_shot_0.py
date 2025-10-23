
from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    # Ensure both strings are of the same length
    if len(a) != len(b):
        raise ValueError("Both strings must be of the same length")
    # Convert each character to int, perform XOR, then convert back to string
    result = ''.join(str(int(char_a) ^ int(char_b)) for char_a, char_b in zip(a, b))
    return result