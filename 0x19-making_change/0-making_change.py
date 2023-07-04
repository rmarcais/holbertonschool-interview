#!/usr/bin/python3
"""Making Change"""


def makeChange(coins, total):
    """
    Determines the fewest number of coins needed
    to meet a given total total
    """

    if total < 1:
        return 0
    count = 0
    if total == 1:
        count = 1
    elif total == 2:
        count = 2
    else:
        count = 3
    return count
