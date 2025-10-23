
from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """Insert a number 'delimeter' between every two consecutive elements of input list `numbers'"""
    result = []
    for num in numbers:
        result.append(num)
        result.append(delimeter)
    # Remove the trailing delimiter if the list was not empty
    if numbers:
        result.pop()
    return result


# Example usage:
# intersperse([1, 2, 3], 4) returns [1, 4, 2, 4, 3]