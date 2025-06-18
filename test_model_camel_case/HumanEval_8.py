# HumanEval/8
from typing import List, Tuple

def sumProduct(numbers: List[int]) -> Tuple[int, int]:
    """ For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.
    """
    totalSum = 0
    totalProduct = 1
    for num in numbers:
        totalSum += num
        totalProduct *= num
    return (totalSum, totalProduct)
