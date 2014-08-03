def solution(n):
    """
    calculate the nth Fibonacci
    >>> solution(6)
    8
    >>> solution(100)
    354224848179261915075L
    >>> solution(300)
    222232244629420445529739893461909967206666939096499764990979600L
    """
    fib = {0: 0, 1: 1}

    def compute_fib(n):
        """
        generate Fibonaci number
        """
        try:
            return fib[n]
        except KeyError:
            fib[n] = compute_fib(n-1) + compute_fib(n-2)
            return fib[n]

    return compute_fib(n)
