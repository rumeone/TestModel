from typing import List, Optional


def longest(strings: List[str]) -> Optional[str]:
    """Return the longest string from *strings*.

    The function scans the list and keeps the first string that has the maximum length.
    If the list is empty, ``None`` is returned.

    >>> longest([])
    >>> longest(['a', 'b', 'c'])
    'a'
    >>> longest(['a', 'bb', 'ccc'])
    'ccc'
    """
    if not strings:
        return None

    # Initialise with the first element
    longest_str = strings[0]
    max_len = len(longest_str)

    for s in strings[1:]:
        if len(s) > max_len:
            longest_str = s
            max_len = len(s)

    return longest_str