# HumanEval/5
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """Insert a number 'delimeter' between every two consecutive elements of input list `numbers'."""
    if not numbers:
        return []
    result = []
    for num in numbers:
        result.append(num)
        result.append(delimeter)
    # Remove the last added delimeter since it's not needed after the last element
    result.pop()
    return result
