# HumanEval/14
def allPrefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string """
    assert isinstance(string, str), "invalid inputs"
    result = []
    for i in range(len(string)):
        result.append(string[:i+1])
    return result
