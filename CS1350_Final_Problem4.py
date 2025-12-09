def recursive_power(x, n):
    """
    Calculate x raised to the power n using recursion.
    n must be a non-negative integer.
    """

    if n == 0:
        return 1
    return x * recursive_power(x, n - 1)


