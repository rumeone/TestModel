from typing import List

def all_prefixes(string: str) -> List[str]:
    """Return list of all prefixes from shortest to longest of the input string.

    Args:
        string: The input string.

    Returns:
        A list of prefixes, starting with the shortest (first character) and ending with the full string.

    Examples:
        >>> all_prefixes('abc')
        ['a', 'ab', 'abc']
    """
    # If the input string is empty, return an empty list.
    if not string:
        return []

    # Build prefixes by progressively adding one more character.
    prefixes: List[str] = []
    for i in range(1, len(string) + 1):
        prefixes.append(string[:i])
    return prefixes