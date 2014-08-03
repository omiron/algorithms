def solutions(S):
    """Check that a string is properly nested.

        A string is considered properly nested if one of the following is true:
            (1) S is empty
            (2) S has the form "(U)" or "[U]" or "{U}" where U is properly nested
            (3) S has the form "VW" where V and W are properly nested

        Args:
            S (str): An N character long string.

        Returns:
            int: 1 if S is properly nested, 0 if it is not.

        Complexity:
            Time: O(N)
            Space: O(N)
    >>> solutions('')
    1
    >>> solutions('{{}}')
    1
    >>> solutions('{{)}')
    0
    >>> solutions('{{}()}')
    1
    >>> solutions('{{}())')
    0
    """
    stack = []
    brackets = {'{': '}', '[': ']', '(': ')'}

    for x in S:
        if x in brackets:
            stack.append(brackets[x])
        elif x in brackets.values():
            if stack.pop() == x:
                continue
            else:
                return 0
    return 1
