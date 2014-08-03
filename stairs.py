def solution(stairs):
    """
    A child is running up a staircase with n steps, and can hop either 1 step,
    2 steps, or 3 steps at a time. Implement a method to count how many
    possible ways the child can run up the stairs.
    >>> solution(5)
    13
    >>> solution(3)
    4
    >>> solution(7)
    44
    """
    map_solution = {1: 1, 2: 2, 3: 4}

    def calculate(stairs):
        try:
            return map_solution[stairs]
        except KeyError:
            return (calculate(stairs - 1) + calculate(stairs - 2) +
                    calculate(stairs - 3))

    return calculate(stairs)
