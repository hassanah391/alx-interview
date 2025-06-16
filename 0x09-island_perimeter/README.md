# 0x09-island_perimeter

This project contains a Python function that calculates the perimeter of an island represented in a 2D grid.

## Task Description

Implement a function `island_perimeter(grid)` that returns the perimeter of the island described in `grid`.

### Requirements

- The grid is a list of list of integers:
  - `0` represents water.
  - `1` represents land.
- Each cell is square with a side length of 1.
- Cells are connected **horizontally and vertically** (not diagonally).
- The grid is **rectangular**, and its dimensions do not exceed 100x100.
- The grid is **completely surrounded by water**.
- There is **only one island** or nothing at all.
- The island **does not contain lakes** (i.e., water not connected to the surrounding water).

## Example

Given the following grid:

```python
grid = [
    [0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0]
]

```

Calling island_perimeter(grid) will return 12

## Usage
To test the function, use the following script (0-main.py).