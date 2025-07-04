# HumanEval/12
from typing import List, Optional


def longest(strings: List[str]) -> Optional[str]:
    """ Return the longest string from the list, or None if the list is empty. """
    if not strings:
        return None
    max_length = 0
    longest_string = strings[0]
    for s in strings:
        if len(s) > max_length:
            max_length = len(s)
            longest_string = s
    return longest_string
