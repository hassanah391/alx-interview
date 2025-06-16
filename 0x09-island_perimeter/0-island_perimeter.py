def island_perimeter(grid):
    """Returns the perimeter of the island described in the grid."""
    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # Start with 4 sides for each land cell
                perimeter += 4

                # Subtract sides shared with adjacent land cells
                if i > 0 and grid[i - 1][j] == 1:  # up
                    perimeter -= 2
                if j > 0 and grid[i][j - 1] == 1:  # left
                    perimeter -= 2

    return perimeter
