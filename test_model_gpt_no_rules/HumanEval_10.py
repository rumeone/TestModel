def is_palindrome(string: str) -> bool:
    """Test if given string is a palindrome"""
    return string == string[::-1]


def make_palindrome(string: str) -> str:
    """Find the shortest palindrome that begins with a supplied string.
    Algorithm idea is simple:
    - Find the longest postfix of supplied string that is a palindrome.
    - Append to the end of the string reverse of a string prefix that comes before the palindromic suffix.
    >>> make_palindrome('')
    ''
    >>> make_palindrome('cat')
    'catac'
    >>> make_palindrome('cata')
    'catac'
    """
    assert type(string) == str, "invalid inputs"

    # Find longest palindromic suffix
    longest_suffix = ""
    for i in range(len(string), -1, -1):
        suffix = string[i:]
        if suffix == suffix[::-1]:
            longest_suffix = suffix
            break

    # Prefix before the suffix
    prefix = string[:len(string) - len(longest_suffix)]
    # Append reverse of prefix
    return string + prefix[::-1]
