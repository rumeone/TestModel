"""
Utility functions for string manipulation.
"""

from typing import List


def all_prefixes(string: str) -> List[str]:
    """Return list of all prefixes from shortest to longest of the input string.

    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    prefixes: List[str] = []  # list to collect prefixes
    for i in range(1, len(string) + 1):  # iterate over prefix lengths
        prefixes.append(string[:i])  # slice up to i
    return prefixes