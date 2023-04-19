#!/usr/bin/python3
"""Rain module"""


def rain(walls):
    """
    Function that calculates how many square units
    of water will be retained after it rains
    """
    if not walls or len(walls) == 0:
        return 0

    result = 0
    wall_height = 0
    rain = 0
    for wall in walls:
        if wall == 0:
            rain += 1
        else:
            result += min(wall_height, wall) * rain
            rain = 0
            wall_height = wall
    return result
