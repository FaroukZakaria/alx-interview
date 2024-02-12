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

N = int(sys.argv[1])
the_end = 0
def clear(x, y, N):
    """
    Clears the boards that are occupied by queen
    on a position given by (x,y) in NxN board
    """
    if ((x > N - 1) or (y > N - 1) or (x < 0) or (y < 0)):
        return

    positions = set()
    for i in range(N):
        positions.add((i, y))  # Horizontal occupied
        positions.add((x, i))  # Vertical occupied

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


def remove_matching_lists(main_list, remove_list):
    return [lst for lst in main_list if lst not in remove_list]


occupied = []
current = []
solutions = []
i = 0
j = 0
while i < N:
    while j < N:
        #print("blay")
        if ([i, j] in occupied):
            if j == N - 1:
                i -= 1
                occupied = occupied[:-(len(clear(i, current[-1][-1], N)))]
                j = current[-1][-1]
                current.pop()
                if j == N - 1:
                    if i == 0:
                        the_end = 1
                        break
                    else:
                        i -= 1
                        occupied = occupied[:-(len(clear(i, current[-1][-1], N)))]
                        j = current[-1][-1]
                        current.pop()
                        j += 1
                        continue
                else:
                    j += 1
                    continue
            else:
                j += 1
                continue
        else:
            #print("Let's go")
            current.append([i, j])
            if i == N - 1:
                solutions.append(current)
                j = current[0][-1] + 1
                i = 0
                current = []
                occupied = []
                continue
            for elm in clear(i, j, N):
                occupied.append(elm)
            i += 1
            j = 0
            break
    #print("blax")
    if the_end == 1:
        break

for i in solutions:
    print(i)
