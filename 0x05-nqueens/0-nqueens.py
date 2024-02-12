#!/usr/bin/python3
"""
N queens puzzle. Place N numbers of queens in NxN board
without them threatening each other.
"""

import sys


if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

try:
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)
except ValueError:
    print("N must be a number")
    sys.exit(1)

def clear(x,y,N):
    """
    Clears the boards that are occupied by queen
    on a position given by (x,y) in NxN board
    """
    if ((x > N - 1) or (y > N - 1) or (x < 0) or (y < 0)):
        return

    positions = set()
    for i in range(N):
        positions.add((i,y))  # Horizontal occupied
        positions.add((x,i))  # Vertical occupied

    X = x
    Y = y
    while ((X >= 0) and (Y <= 3)):  # Up-left diagonal
        positions.add((X, Y))
        X -= 1
        Y += 1
    
    X = x
    Y = y
    while ((X >= 0) and (Y >= 0)):  # Bottom-left diagonal
        positions.add((X, Y))
        X -= 1
        Y -= 1

    X = x
    Y = y
    while ((X <= 3) and (Y <= 3)):  # Top-right diagonal
        positions.add((X, Y))
        X += 1
        Y += 1
    
    X = x
    Y = y
    while ((X <= 3) and (Y >= 0)):  # Bottom-right diagonal
        positions.add((X, Y))
        X += 1
        Y -= 1

    return [list(t) for t in positions]