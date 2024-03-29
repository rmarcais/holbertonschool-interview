#!/usr/bin/python3
"""Island perimeter"""


def island_perimeter(grid):
    """Returns the perimeter of the island described in grid"""
    if not grid:
        return 0

    perimeter = 0
    height = len(grid)
    for i in range(height):
        width = len(grid[i])
        for j in range(width):
            if grid[i][j] == 1:
                if i == 0 or grid[i - 1][j] == 0:
                    perimeter += 1
                if j == 0 or grid[i][j - 1] == 0:
                    perimeter += 1
                if i == height - 1 or grid[i + 1][j] == 0:
                    perimeter += 1
                if j == width - 1 or grid[i][j + 1] == 0:
                    perimeter += 1
    return perimeter
