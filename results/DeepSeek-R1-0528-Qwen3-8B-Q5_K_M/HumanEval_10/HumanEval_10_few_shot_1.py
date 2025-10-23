
def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]

def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string.
    - Find the longest postfix of supplied string that is a palindrome.
    - Append to the end of the string reverse of a string prefix that comes before the palindromic suffix.
    >>> make_palindrome('')
    ''
    >>> make_palindrome('cat')
    'catac'
    >>> make_palindrome('cata')
    'catac'
    """
    # If the string is empty, return empty string
    if string == '':
        return ''
    # Find the longest palindromic suffix
    # Starting from the end, find the longest substring that is a palindrome
    # and is a suffix of the string
    n = len(string)
    # Start from the end and move backwards until we find a palindrome
    for i in range(n, 0, -1):
        if is_palindrome(string[i-1:]):
            # The part before the palindrome is string[:i-1]
            # Reverse that part and append to the beginning
            return string[:i-1] + string[::-1][:i-1:-1]
    # If no palindrome found (should not happen for non-empty string), return the string
    return string