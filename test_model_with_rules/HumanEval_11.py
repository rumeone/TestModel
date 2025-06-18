# HumanEval/11

def string_xor(a: str, b: str) -> str:
    """Perform binary XOR on two strings of 1s and 0s and return the result as a string."""
    if len(a) != len(b):
        raise ValueError("Both strings must have the same length")
    if not all(c in '01' for c in a) or not all(c in '01' for c in b):
        raise ValueError("Both strings must contain only '0' and '1'")
    return ''.join('1' if bit_a == bit_b else '0' for bit_a, bit_b in zip(a, b))
