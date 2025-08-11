"""
Utility module for string filtering operations.
"""

from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """Filter an input list of strings only for ones that contain given substring."""
    assert isinstance(strings, list), "invalid inputs"
    assert all(isinstance(x, str) for x in strings), "invalid inputs"
    assert isinstance(substring, str), "invalid inputs"
    return [s for s in strings if substring in s]
