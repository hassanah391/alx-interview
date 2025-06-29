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
        int: fewest number of coins needed to meet total,
        or -1 if not possible.
    """
    if total <= 0:
        return 0
    rem = total
    coins_count = 0
    coin_idx = 0
    sorted_coins = sorted(coins, reverse=True)
    n = len(coins)
    while rem > 0:
        if coin_idx >= n:
            return -1
        if rem - sorted_coins[coin_idx] >= 0:
            rem -= sorted_coins[coin_idx]
            coins_count += 1
        else:
            coin_idx += 1
    return coins_count
