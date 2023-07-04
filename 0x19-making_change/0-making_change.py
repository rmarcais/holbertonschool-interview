#!/usr/bin/python3
"""Making Change"""


def makeChange(coins, total):
    """
    Determines the fewest number of coins needed
    to meet a given total total
    """
    if total == 0:
        return 0
    count = 0
    for coin in sorted(coins, reverse=True):
        while total >= coin:
            total -= coin
            count += 1
    if total != 0:
        return -1
    return count
