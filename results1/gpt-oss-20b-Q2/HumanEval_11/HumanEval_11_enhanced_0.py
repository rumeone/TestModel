"""
Utility module for binary string operations.
"""

from typing import List


def string_xor(a: str, b: str) -> str:
    """
    Perform a bitwise XOR on two binary strings composed of '0' and '1'.

    Parameters
    ----------
    a : str
        First binary string.
    b : str
        Second binary string.

    Returns
    -------
    str
        Result of XORing each corresponding bit.

    Examples
    --------
    >>> string_xor('010', '110')
    '100'
    """
    # Ensure both strings are of equal length; otherwise raise an error.
    if len(a) != len(b):
        raise ValueError("Input strings must have the same length")

    # Compute XOR for each pair of characters.
    result_bits: List[str] = []
    for bit_a, bit_b in zip(a, b):
        # XOR: '1' if bits differ, otherwise '0'.
        xor_bit = '1' if bit_a != bit_b else '0'
        result_bits.append(xor_bit)

    # Join the list into a single string.
    return ''.join(result_bits)