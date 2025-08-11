def longest(strings):
    """Out of list of strings, return the longest one. Return the first one in case of multiple
    strings of the same length. Return None in case the input list is empty."""
    assert type(strings) == list, "invalid inputs"
    assert all([isinstance(v, str) for v in strings]), "invalid inputs"
    if not strings:
        return None
    longest_str = strings[0]
    max_len = len(longest_str)
    for s in strings[1:]:
        l = len(s)
        if l > max_len:
            longest_str = s
            max_len = l
    return longest_str
