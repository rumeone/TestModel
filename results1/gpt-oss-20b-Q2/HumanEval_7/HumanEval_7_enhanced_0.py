"""
Utility module for string filtering operations.
"""

from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Return a new list containing only those strings that contain the given substring.

    Parameters
    ----------
    strings : List[str]
        Input list of strings to filter.
    substring : str
        Substring to search for in each element.

    Returns
    -------
    List[str]
        List of strings that contain the substring.

    Examples
    --------
    >>> filter_by_substring([], 'a')
    []
    >>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
    ['abc', 'bacd', 'array']
    """
    # Use list comprehension for concise filtering
    return [s for s in strings if substring in s]