#!/usr/bin/python3

def island_perimeter(grid):
    """
    Determines the perimeter of the grid

    Args:
        grid : array of list of 0 or 1 (0 for water, 1 for land)

    Returns:
        int of the perimeter
    """
    # result will be the total perimeter of the island
    result = 0
    # for loop to test all sides of an island square
    for linepos, line in enumerate(grid):
        for keypos, cell in enumerate(line):
            if cell == 1:
                total = 0
                top = grid[linepos - 1][keypos]
                bottom = grid[linepos + 1][keypos]
                right = line[keypos + 1]
                left = line[keypos - 1]
                total = 4 - (top + bottom + right + left)
                result += total
    # return result of the perimeter
    return result
