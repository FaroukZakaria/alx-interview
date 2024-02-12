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

    for i in range(N):
        positions.add((x, i))  # Vertical occupied

    X = x
    Y = y
    while ((X >= 0) and (Y < N)):  # Up-left diagonal
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
    while ((X < N) and (Y < N)):  # Top-right diagonal
        positions.add((X, Y))
        X += 1
        Y += 1

    X = x
    Y = y
    while ((X < N) and (Y >= 0)):  # Bottom-right diagonal
        positions.add((X, Y))
        X += 1
        Y -= 1

    return [list(t) for t in positions]


occupied = []
current = []
solutions = []
i = 0
j = 0
while i < N:
    #print(f"current: \n{current}\n")
    #print(f"occupied: \n{occupied}\n")
    #print(f"solution: \n{solutions}\n")
    while j < N:
        #print(f"current: \n{current}\n")
        if ([i, j] in occupied):
            if j == N - 1:  # Check if y-position is at top
                i -= 1
                occupied = occupied[:-(len(clear(i, current[-1][-1], N)))]
                j = current[-1][-1]
                current.pop()
                if j == N - 1:  # Check if y-position at top after change
                    if i == 0:  # Check if x-position at start (all done)
                        the_end = 1
                        break
                    else:  # There are more possibilities
                        i -= 1
                        occupied = occupied[:-(len(clear(
                            i,
                            current[-1][-1], N)))]
                        j = current[-1][-1]
                        current.pop()
                        j += 1
                        continue
                else:  # if y not at top
                    j += 1
                    continue
            else:  # if y not at top
                j += 1
                continue
        else:  # Not occupied
            current.append([i, j])  # mark the point
            if i == N - 1:  # Checks if all queens are placed
                solutions.append(current[:])  # Add the solution
                print(f"solution{len(solutions)} is: ")
                print(solutions)
                j = current[-1][-1]
                current.pop()
                print(f"solution{len(solutions)} before if is: ")
                print(solutions)
                if j == N - 1:
                    i -= 1
                    occupied = occupied[:-(len(clear(
                            i,
                            current[-1][-1], N)))]
                    j = current[-1][-1]
                    current.pop()
                    j += 1
                    print(f"solution{len(solutions)} after if is: ")
                    print(solutions)
                    continue
                else:
                    j += 1
                    continue
            for elm in clear(i, j, N):  # mark all the occupied squares
                occupied.append(elm)
            i += 1
            j = 0
            break
    if the_end == 1:
        break

for i in solutions:
    print(i)
