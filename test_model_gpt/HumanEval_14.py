"""
Utility functions for string manipulation.
"""

from typing import List


def all_prefixes(string: str) -> List[str]:
    """Return list of all prefixes from shortest to longest of the input string.

    Examples:
        >>> all_prefixes('abc')
        ['a', 'ab', 'abc']
    """
    assert isinstance(string, str), "invalid inputs"
    return [string[:i] for i in range(1, len(string) + 1)]
