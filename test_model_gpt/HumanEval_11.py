"""
Utility module for binary string operations.
"""

def string_xor(a: str, b: str) -> str:
    """Perform binary XOR on two equal-length strings of '0' and '1'.

    Parameters
    ----------
    a : str
        First binary string.
    b : str
        Second binary string.

    Returns
    -------
    str
        Result of XOR operation as a string.

    Examples
    --------
    >>> string_xor('010', '110')
    '100'
    """
    assert isinstance(a, str) and isinstance(b, str), "invalid inputs"
    assert len(a) == len(b), "invalid inputs"
    assert set(a).issubset({"0", "1"}), "invalid inputs"
    assert set(b).issubset({"0", "1"}), "invalid inputs"

    result = []
    for bit_a, bit_b in zip(a, b):
        xor_bit = '1' if bit_a != bit_b else '0'
        result.append(xor_bit)
    return ''.join(result)
