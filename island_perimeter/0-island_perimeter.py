#!/usr/bin/python3
"""
0-island_perimeter module:
Given a grid of integers representing water (0) and land (1),
computes and returns the perimeter of the island.

The grid is rectangular, surrounded by water, with at most one island.
"""


def island_perimeter(grid):
    """
    Determines the perimeter of the island in the grid.

    Args:
        grid (list of list of int):
            2D list where 0 represents water and 1 represents land.
    Returns:
        int: perimeter of the island (sum of exposed sides of land cells).
    """
    result = 0

    # Iterate over each cell to count exposed sides
    for row_idx, row in enumerate(grid):
        for col_idx, cell in enumerate(row):
            if cell == 1:
                # Top side
                if row_idx == 0 or grid[row_idx - 1][col_idx] == 0:
                    result += 1
                # Bottom side
                if row_idx == len(grid) - 1 or grid[row_idx + 1][col_idx] == 0:
                    result += 1
                # Left side
                if col_idx == 0 or row[col_idx - 1] == 0:
                    result += 1
                # Right side
                if col_idx == len(row) - 1 or row[col_idx + 1] == 0:
                    result += 1

    return result
