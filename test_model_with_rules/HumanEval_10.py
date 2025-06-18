# HumanEval/10
def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]

def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string.
    Algorithm idea is simple:
    - Find the longest postfix of supplied string that is a palindrome.
    - Append to the end of the string reverse of a string prefix that comes before the palindromic suffix.
    """
    # If the string is empty, return empty string
    if string == '':
        return ''
    # Find the longest palindromic suffix
    # Start from the end and move backwards until the substring is a palindrome
    for i in range(len(string), 0, -1):
        if is_palindrome(string[i-1:]):
            # The part before the palindromic suffix is the prefix to be mirrored
            prefix = string[:i-1]
            # Return the mirrored string: prefix + palindromic part + reverse(prefix)
            return prefix + string
    # If no palindrome found, return the string plus its reverse
    return string + string[::-1]
