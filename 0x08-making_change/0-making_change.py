#!/usr/bin/python3
"""
This module contains the makeChange function.
"""


def makeChange(coins, total):
    """
    Determines the fewest number of coins needed to meet a given amount total.
    Args:
        coins (list): list of the values of the coins in your possession.
        total (int): the total amount.
    Returns:
        int: fewest number of coins needed to meet total, or -1 if not possible.
    """
        if not coins or coins is None:
        return -1
    if total <= 0:
        return 0
    change = 0
    coins = sorted(coins)[::-1]
    for coin in coins:
        while coin <= total:
            total -= coin
            change += 1
        if (total == 0):
            return change
    return -1

