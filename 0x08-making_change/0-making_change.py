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

    impossible = 1
    for i in coins:
        if total % i == 0:
            impossible = 0
            break

    if impossible:
        return -1

    sorted_coins = sorted(coins)
    total_coins = total
    print(f"Calculating for coins: {sorted_coins}")
    number_of_coins = 0
    for i in range(-1, len(sorted_coins) * -1, -1):
        print(f"calculating {total_coins} / {sorted_coins[i]}")
        number_of_coins += (total_coins // sorted_coins[i])
        print(f"subtracting "
                f"{(total_coins // sorted_coins[i]) * sorted_coins[i]} "
                f"from total coins")
        total_coins -= (total_coins // sorted_coins[i]) * sorted_coins[i]
        print(f"and total coins now are {total_coins}")
        print(f"number of coins is now: {number_of_coins}")

    return number_of_coins
