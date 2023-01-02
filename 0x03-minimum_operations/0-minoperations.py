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
    rem = n

    # We search the prime factors of n and each time
    # we find one, we add it to minOperations
    while (rem > 1):
        if (rem % 2 == 0):
            minOperations += 2
            rem //= 2
        else:
            i = 3
            while(i * i <= rem):
                if (rem % i == 0):
                    minOperations += i
                    rem /= i
                    break
                i += 2
            minOperations += rem
            rem /= rem
    return int(minOperations)
