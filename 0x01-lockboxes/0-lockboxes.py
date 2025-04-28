#!/usr/bin/python3
"""
Lockboxes Module

This module contains a function that solves the 'lockboxes' problem.
In this problem, we have n number of locked boxes, each numbered sequentially
from 0 to n-1. Each box may contain keys to other boxes. A key with the same
number as a box opens that box. The goal is to determine if all boxes can
be opened, starting with box 0 which is initially unlocked.
"""


def canUnlockAll(boxes):
    """
    Determines if all locked boxes can be opened.

    Each box is numbered sequentially from 0 to n - 1 and may contain keys to
    other boxes. A key with the same number as a box opens that box.
    Box 0 is unlocked by default.

    Args:
        boxes (list): A list of lists where each inner list contains keys
                     (integers) that can open other boxes.

    Returns:
        bool: True if all boxes can be opened, False otherwise.

    Raises:
        TypeError: If boxes is not a list.
    """
    if not isinstance(boxes, list):
        raise TypeError('Boxes must be a list')

    unlocked = set([0])  # start with box 0 unlocked
    keys = list(boxes[0])  # keys we initially have

    while keys:
        key = keys.pop()
        if 0 <= key < len(boxes) and key not in unlocked:
            unlocked.add(key)
            keys.extend(boxes[key])  # add new keys from the newly unlocked box

    return len(unlocked) == len(boxes)
