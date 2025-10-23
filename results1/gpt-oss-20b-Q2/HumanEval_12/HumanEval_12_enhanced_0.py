"""
Utility module for string list operations.
"""

from typing import List, Optional


def longest(strings: List[str]) -> Optional[str]:
    """Return the longest string from *strings*.

    If multiple strings share the maximum length, the first one is returned.
    If *strings* is empty, ``None`` is returned.

    >>> longest([])
    >>> longest(['a', 'b', 'c'])
    'a'
    >>> longest(['a', 'bb', 'ccc'])
    'ccc'
    """
    if not strings:  # empty list
        return None

    # initialise with first element
    longest_str = strings[0]
    max_len = len(longest_str)

    for s in strings[1:]:
        l = len(s)
        if l > max_len:  # found longer string
            longest_str = s
            max_len = l
    # return the longest found
    return longest_str