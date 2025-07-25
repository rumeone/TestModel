# HumanEval/9
from typing import List, Tuple

def rollingMax(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    if not numbers:
        return []
    currentMax = numbers[0]
    result = [currentMax]
    for num in numbers:
        if num > currentMax:
            currentMax = num
            result.append(currentMax)
        else:
            result.append(currentMax)
    return result
