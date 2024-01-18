#!/usr/bin/python3

def minOperations(n):
    """
    Calculates the minimum number of operations (Copy All and Paste) required to
    achieve exactly n H characters in a text file, starting with a single H.
    Args:
        n: The target number of H characters.
    Returns:
        The minimum number of operations required, or 0 if n is not achievable.
    """

    if n == 1:
        return 0

    ops = 0
    while n % 2 == 0:
        n //= 2
        ops += 1

    # Check if any odd number greater than 1 can be formed
    if n > 1:
        return ops + n

    # Otherwise, n is not achievable
    return 0

