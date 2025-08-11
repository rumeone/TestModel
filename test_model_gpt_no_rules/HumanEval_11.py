def string_xor(a: str, b: str) -> str:
    """Perform binary XOR on two equal-length strings of '0' and '1'.

    Args:
        a (str): First binary string.
        b (str): Second binary string.

    Returns:
        str: Result of XOR operation.

    Example:
        >>> string_xor('010', '110')
        '100'
    """
    # Contract checks
    assert isinstance(a, str) and isinstance(b, str), "invalid inputs"
    assert len(a) == len(b), "invalid inputs"
    assert set(a).issubset({"0", "1"}), "invalid inputs"
    assert set(b).issubset({"0", "1"}), "invalid inputs"

    # Perform XOR
    result_chars = []
    for char_a, char_b in zip(a, b):
        if char_a == char_b:
            result_chars.append('0')
        else:
            result_chars.append('1')
    return ''.join(result_chars)
