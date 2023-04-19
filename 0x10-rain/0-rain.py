#!/usr/bin/python3
"""Rain module"""


def rain(walls):
    """
    Function that calculates how many square units
    of water will be retained after it rains
    """
    size = len(walls)
    if size == 0:
        return 0

    result = 0

    for i in range(1, size - 1):
        left = walls[i]
        for j in range(i):
            left = max(left, walls[j])

        right = walls[i]
        for j in range(i + 1, size):
            right = max(right, walls[j])

        result = result + (min(left, right) - walls[i])
    return result
