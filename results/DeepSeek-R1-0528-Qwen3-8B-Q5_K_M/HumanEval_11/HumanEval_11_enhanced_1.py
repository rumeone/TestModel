from typing import List


def string_xor(a: str, b: str) -> str:
    """Perform binary XOR on two strings of 1s and 0s and return the result as a string.

    Args:
        a: Input string of 1s and 0s.
        b: Input string of 1s and 0s.

    Returns:
        A string representing the binary XOR result.

    Example:
        >>> string_xor('010', '110')
        '100'
    """
    # Ensure both strings are of the same length by padding the shorter one with zeros
    # at the beginning (left side) to match the length of the longer string.
    # This is done by calculating the difference in lengths and adjusting accordingly.
    if len(a) > len(b):
        b = b.zfill(len(a))
    elif len(b) > len(a):
        a = a.zfill(len(b))
    else:
        # If both strings are of the same length, proceed with the XOR.
        # For each position, convert the characters to integers, perform XOR,
        # then convert back to string.
        result = []
        for i in range(len(a)):
            # Convert each character to int and XOR them, then convert back to string.
            result.append(str(int(a[i]) ^ int(b[i])))
        return ''.join(result)
    # If one string is longer, we need to pad the shorter one with zeros on the left.
    # Then perform the XOR for each position, starting from the leftmost character.
    result = []
    for i in range(len(a)):
        # Convert each character to int and XOR them, then convert back to string.
        result.append(str(int(a[i]) ^ int(b[i])))
    return ''.join(result)