# HumanEval/11
def string_xor(a: str, b: str) -> str:
    """Perform binary XOR on two strings a and b containing only '0' and '1' characters."""
    assert isinstance(a, str) and isinstance(b, str), "invalid inputs"
    assert len(a) == len(b), "invalid inputs"
    assert set(a).issubset({"0", "1"}) and set(b).issubset({"0", "1"}), "invalid inputs"
    result = []
    for i in range(len(a)):
        if a[i] == b[i]:
            result.append('0')
        else:
            result.append('1')
    return ''.join(result)
