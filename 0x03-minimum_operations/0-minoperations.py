#!/usr/bin/python3
"""Interview 3: Minimum Operations"""


def minOperations(n):
    """
    Method that calculates the fewest number of operations
    needed to result in exactly n H characters in the file.
    """

    if n <= 1:
        return 0

    minOperations = 0

    # We search the prime factors of n and each time
    # we find one, we add it to minOperations
    while (n > 1):
        if (n % 2 == 0):
            minOperations += 2
            n //= 2
        else:
            i = 3
            while(i * i <= n):
                if (n % i == 0):
                    minOperations += i
                    n /= i
                    break
                i += 2
            minOperations += n
            n /= n
    return int(minOperations)
