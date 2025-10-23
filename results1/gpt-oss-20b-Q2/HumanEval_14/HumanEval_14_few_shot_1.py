from typing import List


def all_prefixes(string: str) -> List[str]:
    """Return a list of all prefixes of *string*, ordered from shortest to longest.

    The function builds each prefix by progressively slicing the input string from the first character up to the current index.

    Parameters
    ----------
    string : str
        The string to generate prefixes from.

    Returns
    -------
    List[str]
        A list containing every prefix of *string*, starting with the first character and ending with the full string.

    Examples
    --------
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    >>> all_prefixes('')
    []
    """
    # Handle the trivial case of an empty string early.
    if not string:
        return []

    # Build prefixes by slicing from the start up to each index.
    prefixes: List[str] = []
    for i in range(1, len(string) + 1):
        prefixes.append(string[:i])
    return prefixes