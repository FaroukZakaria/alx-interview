#!/usr/bin/python3
"""
This module gives the fewest number of coins needed to make up a total
"""


def makeChange(coins, total):
    """
    The function that makes up a total from given coins

    coins argument is a list
    list items can be chosen more than once
    if "total" is 0 or less then 0 is returned
    if it's impossible to get total from given coins, -1 is returned
    """

    if total <= 0:
        return 0

    sorted_coins = sorted(coins)  # Sorting to start counting
    total_coins = total  # another variable pointing to total for modification
    number_of_coins = 0  # The number that will be returned
    for i in range(-1, len(sorted_coins) * -1 - 1, -1):  # from high to low
        # adding all possible whole numbers of the current coin
        number_of_coins += (total_coins // sorted_coins[i])
        # Subtracting what I gathered from the recent operation
        total_coins -= (total_coins // sorted_coins[i]) * sorted_coins[i]

        if total_coins == 0:  # I succeeded in collecting them if they're zero
            return number_of_coins

    return -1  # If total_coins still 0, then it's impossible to get required
