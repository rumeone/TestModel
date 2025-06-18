# HumanEval/11
from typing import List

def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    # Check if inputs are strings and contain only '0' and '1'
    if not isinstance(a, str) or not isinstance(b, str):
        raise TypeError("invalid inputs")
    if len(a) != len(b):
        raise ValueError("invalid inputs")
    if not all(c in '01' for c in a) or not all(c in '01' for c in b):
        raise ValueError("invalid inputs")
    
    result = []
    for i in range(len(a)):
        # Convert each character to integer and perform XOR
        bit_a = int(a[i])
        bit_b = int(b[i])
        xor_bit = bit_a ^ bit_b
        result.append(str(xor_bit))
    
    return ''.join(result)

