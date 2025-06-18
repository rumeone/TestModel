# HumanEval/11
from typing import List

def string_xor(a: str, b: str) -> str:
    """Perform binary XOR on two strings a and b containing only '0' and '1' characters.
    Each character in the result is the XOR of the corresponding characters in a and b.
    """
    assert isinstance(a, str) and isinstance(b, str), "invalid inputs"
    assert len(a) == len(b), "invalid inputs"
    assert all(c in '01' for c in a) and all(c in '01' for c in b), "invalid inputs"
    
    result = []
    for i in range(len(a)):
        if a[i] == b[i]:
            result.append('0')
        else:
            result.append('1')
    return ''.join(result)
