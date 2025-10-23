def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]


def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string.
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
    if not string:
        return ''
    n = len(string)
    # Find the longest suffix that is a palindrome
    longest_suffix = ''
    for i in range(n, -1, -1):
        suffix = string[i:]
        if is_palindrome(suffix):
            longest_suffix = suffix
            break
    # Prefix before the palindrome suffix
    prefix = string[:n - len(longest_suffix)]
    # Append reverse of the prefix to the end
    return string + prefix[::-1]