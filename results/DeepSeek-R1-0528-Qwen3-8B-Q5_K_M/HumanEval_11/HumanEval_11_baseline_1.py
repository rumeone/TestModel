from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    result = []
    # Ensure both strings are of the same length by padding the shorter one with '0's at the beginning
    n = max(len(a), len(b))
    a = a.zfill(n)
    b = b.zfill(n)
    for bit1, bit2 in zip(a, b):
        if bit1 == bit2:
            result.append('0')
        else:
            result.append('1')
    return ''.join(result)