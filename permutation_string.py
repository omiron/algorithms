def solution(S1, S2):
    """
    Given two strings, write a method to decide if one is a permutation of the
    other.

    >>> solution("abcde", "baced")
    True
    >>> solution("abde", "baced")
    False
    >>> solution("", "baced")
    False
    """
    def get_map(S):
        d = {}
        for ch in S:
            d[ch] = d.get(ch, 0) + 1
        return d

    if get_map(S1) == get_map(S2):
        return True
    return False
