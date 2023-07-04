#!/usr/bin/python3
"""
makeChange method
"""


def makeChange(coins, total):
    """Determine the fewest number of coins."""
    # scoins = sorted(coins, reverse=True)
    # return rec_change(scoins, total, 0, 0, -1)
    i = 0
    for coin in coins:
        j = total // coin
        total -= j * coin
        i += j
        if total <= 0:
            break

    if total != 0:
        i = -1

    return i
