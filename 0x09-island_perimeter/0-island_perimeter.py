#!/usr/bin/python3
"""
This module calculates perimeter of an island represented by 1's
in water represented by 0's. There's only one island (or nothing).

Each "1" is a square with edge length of 1 unit.
"""


def island_perimeter(grid):
    """
    Calculates the perimeter of an island using a grid with 100 area units max
    """
    height = len(grid)
    width = len(grid[0])
    if height > 100:
        print("Grid height must not exceed 100")
        return
    elif width > 100:
        print("Grid width must not exceed 100")

    perimeter = 0
    for row in range(height):
        for elm in range(width):
            if grid[row][elm] == 0:
                continue

            edge = 0
            # Check up
            if row != 0:
                if grid[row - 1][elm] == 0:  # There's water above
                    edge += 1
            else:
                edge += 1

            # Check left
            if elm != 0:
                if grid[row][elm - 1] == 0:  # There's water left
                    edge += 1
            else:
                edge += 1

            # Check right
            if elm != width - 1:
                if grid[row][elm + 1] == 0:  # There's water right
                    edge += 1
            else:
                edge += 1

            # Check down
            if row != height - 1:
                if grid[row + 1][elm] == 0:  # There's water below
                    edge += 1
            else:
                edge += 1

            perimeter += edge

    return perimeter
