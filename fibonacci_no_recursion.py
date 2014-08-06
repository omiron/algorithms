def solution(A):
    """
    calculate the nth Fibonacci
    >>> solution(6)
    8
    >>> solution(100)
    354224848179261915075L
    >>> solution(300)
    222232244629420445529739893461909967206666939096499764990979600L
    """
    fib_memorize = {}

    for idx in range(A + 1):
        if idx <= 2:
            f = 1
        else:
            f = fib_memorize[idx - 1] + fib_memorize[idx - 2]
        fib_memorize[idx] = f
    return fib_memorize[A]
