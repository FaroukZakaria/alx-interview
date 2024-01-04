#!/usr/bin/python3
"""
Pascal triangle
"""


def pascal_triangle(n):
    """
    Uses Combination to get the pascal triangle
    """
    if n <= 0:
        return []
    lst = []
    for i in range(n):
        row = []
        for j in range(i + 1):
            row.append(
                (my_factorial(i)) //
                (my_factorial(j) * my_factorial(i - j))
                )
        lst.append(row)
    return lst


def my_factorial(n):
    """
    Custom factorial function
    """
    if n <= 0:
        return 1
    return (n * my_factorial(n-1))
