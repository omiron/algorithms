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
#   m_o means minus one
#   m_t means minus two
    fib_memorize = {'m_o': 1, 'm_t': 1}

    for idx in range(3, A + 1):
        fib_memorize['m_o'], fib_memorize['m_t'] = fib_memorize['m_o'] + \
            fib_memorize['m_t'], fib_memorize['m_o']

    return fib_memorize['m_o']
