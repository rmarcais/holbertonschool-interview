#!/usr/bin/python3
"""Making Change"""


def makeChange(coins, total):
    """
    make change: bottom up method
    """
    if total < 1:
        return 0
    count = 0
    for coin in sorted(coins, reverse=True):
        while total >= coin:
            count += 1
            total -= coin
            if total == 0:
                return count
    return -1
