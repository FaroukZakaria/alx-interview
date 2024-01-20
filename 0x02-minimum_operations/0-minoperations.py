#!/usr/bin/python3
"""
Calculating minimum operations to get 'n' amount of characters (say 'H')
Operations are copying all and pasting only
"""


def minOperations(n):
    """
    Get minimum operations to get n amount of H using modulus operators
    """
    if n <= 1:
        return 0

    chars = 1
    operations = 0
    copied = 1

    while (chars != n):
        if (n % chars == 0):
            operations += 2  # Copying and pasting
            copied = chars  # The new amount copied to be pasted
            chars *= 2
        else:
            operations += 1  # pasting
            chars += copied  # what's pasted

    return operations
