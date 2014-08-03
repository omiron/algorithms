def solution(A):
    """
    A sorted array has been rotated so that the elements might appear in the
    order 3, 4,  5, 6, 7, 1, 2. How would you find the minimum element? You may
    assume that the array has all unique elements.

    >>> solution([3, 1, 2])
    1
    >>> solution([2, 3, 4, 6, 1])
    1
    >>> solution([2, 1])
    1
    """
    if len(A) == 1:
        return A[0]
    if len(A) == 2:
        if A[0] < A[1]:
            return A[0]
        else:
            return A[1]
    middle, rest = divmod(len(A), 2)

    if A[0] > A[middle + rest]:
        min_elem = solution(A[:middle + rest])
    elif A[-1] < A[middle]:
        min_elem = solution(A[middle + rest:])

    return min_elem
