#!/usr/bin/python3
"""
This is a game called "Prime game." It's about picking prime numbers
in a set of consecutive integers from 1 to n, and removing their multiples
The round ends when there are no more prime numbers to pick
and the winner is decided if the loser can not pick a prime in their is turn.

The game ends when there are no more rounds (rounds are in a list of n's)
The winner of the game is the one with the most wins overall (or None if tie)

The players are: Ben, and Maria
Maria always goes first
"""


def is_prime(n):
    """
    Checks if n is prime
    """
    if n % 2 == 0:
        return False

    for i in range(3, int(n ** 0.5) + 1, 2):
        # Iterates over odd numbers from 3 to the square root of n
        if n % i == 0:
            return False

    return True


def len_primes(n):
    """
    Returns the number of prime numbers from 1 to n
    """
    if n <= 1:
        return 0
    elif n == 2:
        return 1

    p = 1  # Number of prime numbers starting from 1 because 2 is counted
    for i in range(3, n + 1):  # Iterates from to n (included)
        if is_prime(i):
            p += 1

    return p


def isWinner(x, nums):
    """
    Returns the winner of the game (or None if tie)
    """
    if x > len(nums):  # number of rounds is more than given n for each round
        return None

    if nums == []:  # Empty list means no given n to play the game
        return None

    if not isinstance(nums, list):  # if nums isn't a list
        return None

    """for i in range(len(nums)):  # Check if any list item is not an integer
        if not isinstance(nums[i], int):
            return None"""
    Ben = 0
    Maria = 0
    for i in range(x):
        try:
            if len_primes(nums[i]) % 2 == 0:
                # If there are even number of primes, Ben wins
                # Removing the multiple of numbers does nothing
                # Because multiples are not primes because, they're multiples.
                Ben += 1
            else:
                Maria += 1
        except Exception:
            continue

    if Ben == Maria:
        return None

    if Ben > Maria:
        return "Ben"
    else:
        return "Maria"
