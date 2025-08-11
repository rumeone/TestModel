# Imports
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """Return the longest string from a list of strings, or None if empty."""
    assert type(strings) == list, "invalid inputs"
    assert all([isinstance(v, str) for v in strings]), "invalid inputs"
    if not strings:
        return None
    longest_str = strings[0]
    for s in strings[1:]:
        if len(s) > len(longest_str):
            longest_str = s
    return longest_str
