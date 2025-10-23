from typing import List


def string_xor(a: str, b: str) -> str:
    """Perform a bitwise XOR on two binary strings.

    Parameters
    ----------
    a : str
        First binary string consisting only of characters '0' and '1'.
    b : str
        Second binary string of the same length as ``a``.

    Returns
    -------
    str
        Result of the XOR operation, also as a binary string.

    Examples
    --------
    >>> string_xor('010', '110')
    '100'
    """
    if len(a) != len(b):
        raise ValueError("Input strings must have the same length")

    # Perform XOR bit by bit
    result = ''.join('1' if x != y else '0' for x, y in zip(a, b))
    return result