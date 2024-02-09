#!/usr/bin/python3
"""
N queens puzzle. Place N numbers of queens in NxN board
without them threatening each other.
"""

import sys


if len(sys.argv) != 2:
    print("usage: nqueens N")
    sys.exit(1)

try:
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)
except ValueError:
    print("N must be a number")
    sys.exit(1)
