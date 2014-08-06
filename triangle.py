def solution(A):
    """
    Let be a triagle like below:
    2
    1 5
    1 3 4
    9 1 1 6

    Calculate the maximum sum you can optain from up to down follows the rules:
        1. sum is calculate starting from up to down.
        2. sum += A[i-1, j-1]  or sum += A[i+1, j]

    >>> solution([[2, 0, 0, 0], [1, 5, 0, 0], [1, 3, 4, 0], [9, 1, 1, 6]])
    17
    """
    l = len(A) - 1
    for idx in range(len(A) - 2, -1, -1):
        for jdx in range(0, l):
            A[idx][jdx] = A[idx][jdx] + max(A[idx + 1][jdx],
                                            A[idx + 1][jdx + 1])
        l -= 1
    return A[0][0]
