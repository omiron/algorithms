def solution(A):
    """
    Find the who is unique and have minimum index in A. If not exist such
    number returns -1.
    >>> solution([1, 4, 3, 3, 1, 2])
    4
    >>> solution([6, 4, 4, 6])
    -1
    >>> solution([])
    -1
    """
    d = {}
    for idx, nr in enumerate(A):
        try:
            if d[nr] != -1:
                d[nr] = -1
        except KeyError:
            d[nr] = idx

    min_idx = len(A)
    for number, idx in d.items():
        if idx != -1 and min_idx > idx:
            min_idx = idx

    if min_idx < len(A):
        return A[min_idx]
    return -1
