from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """Return the longest string from a list of strings.

    If multiple strings have the same maximum length, the first one is returned.
    If the input list is empty, None is returned.

    >>> longest([])
    None
    >>> longest(['a', 'b', 'c'])
    'a'
    >>> longest(['a', 'bb', 'ccc'])
    'ccc'
    """
    if not strings:
        return None
    # max will return the first string with the maximum length
    return max(strings, key=len)