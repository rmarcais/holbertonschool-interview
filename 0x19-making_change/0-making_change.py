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
    for coin in coins:
        while total >= coin:
            total -= coin
            count += 1
    return count
