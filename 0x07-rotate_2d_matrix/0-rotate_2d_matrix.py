#!/usr/bin/python3
"""
Rotating matrices by 90° clockwise
"""


def reverse(matrix, start, end):
    """
    recursively reverses a list
    """
    if start >= end:
        return
    matrix[start], matrix[end] = matrix[end], matrix[start]
    reverse(matrix, start + 1, end - 1)


def transpose(matrix):
    """
    Switches rows and columns
    """
    new_matrix = []
    for i in range(len(matrix)):
        new_matrix.append([])
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            new_matrix[i].append(0)
    j = 0
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            new_matrix[j][i] = matrix[i][j]

    return new_matrix

def rotate_2d_matrix(matrix):
    """
    rotates the 2D matrix by reversing rows and transposing
    """
    reverse(matrix, 0, len(matrix) - 1)
    new_matrix = transpose(matrix)
    for i in range(len(matrix)):
        matrix[i] = new_matrix[i]
