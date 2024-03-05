#!/usr/bin/python3
"""
This module calculates perimeter of an island represented by 1's
in solid represented by 0's. There's only one island (or nothing).

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
        print(f"checking for row: {row}")
        for elm in range(width):
            if grid[row][elm] == 0:
                continue

            solid = 0
            # Check up
            if row != 0:
                if grid[row - 1][elm] == 0:  # There's water above
                    print("there's water above")
                    solid += 1

            # Check left
            if elm != 0:
                if grid[row][elm - 1] == 0:  # There's water left
                    print("there's water left")
                    solid += 1

            # Check right
            if elm != width - 1:
                if grid[row][elm + 1] == 0:  # There's water right
                    print("there's water right")
                    solid += 1

            # Check down
            if row != height - 1:
                if grid[row + 1][elm] == 0:  # There's water below
                    print("there's water below")
                    solid += 1

            print(f"adding {solid} to perimeter")
            perimeter += solid

    return perimeter
