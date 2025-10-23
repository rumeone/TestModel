from typing import List, Optional


def longest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, return the longest one. Return the first one in case of multiple
    strings of the same length. Return None in case the input list is empty.
    """
    if not strings:
        return None
    # Find the maximum length among the strings
    max_length = max(len(s) for s in strings)
    # Iterate through the list and return the first string with max_length
    for s in strings:
        if len(s) == max_length:
            return s
    # This line should never be reached because there's at least one string
    return None


# Example tests (for verification only, not part of the function)
if __name__ == "__main__":
    print(longest([]) is None)  # True
    print(longest(['a', 'b', 'c']) == 'a')  # True
    print(longest(['a', 'bb', 'ccc']) == 'ccc')  # True