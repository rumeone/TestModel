from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """Insert a number 'delimeter' between every two consecutive elements of input list `numbers`."""
    assert all(isinstance(v, int) for v in numbers), "invalid inputs"
    assert isinstance(delimeter, int), "invalid inputs"

    if not numbers:
        return []

    result: List[int] = []
    for i, value in enumerate(numbers):
        result.append(value)
        if i < len(numbers) - 1:
            result.append(delimeter)
    return result
