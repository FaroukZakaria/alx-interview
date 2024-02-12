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
    while ((X >= 0) and (Y <= N)):  # Up-left diagonal
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
    while ((X <= N) and (Y <= N)):  # Top-right diagonal
        positions.add((X, Y))
        X += 1
        Y += 1

    X = x
    Y = y
    while ((X <= N) and (Y >= 0)):  # Bottom-right diagonal
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
        print("current is now:")
        print(current)
        if ([i, j] in occupied):
            print("occupied")
            if j == N - 1:  # Check if y-position is at top
                print("It's on top as well")
                i -= 1
                occupied = occupied[:-(len(clear(i, current[-1][-1], N)))]
                j = current[-1][-1]
                current.pop()
                print("after going back and undoing, current is now:")
                print(current)
                if j == N - 1:  # Check if y-position at top after change
                    print("the one at back is already at top...")
                    if i == 0:  # Check if x-position at start (all done)
                        print("and it's at first field as well.. game over")
                        the_end = 1
                        break
                    else:  # There are more possibilities
                        print("and there are more possibilities")
                        i -= 1
                        occupied = occupied[:-(len(clear(
                            i,
                            current[-1][-1], N)))]
                        j = current[-1][-1]
                        current.pop()
                        j += 1
                        print("after going back and undoing, current is now:")
                        print(current)
                        continue
                else:  # if y not at top
                    print("moving up")
                    j += 1
                    continue
            else:  # if y not at top
                print("moving up")
                j += 1
                continue
        else:  # Not occupied
            print(f"Not occupied. Marking... {[i,j]}")
            current.append([i, j])  # mark the point
            if i == N - 1:  # Checks if all queens are placed
                print("all queens are placed. Submitting solution:")
                print(current)
                solutions.append(current)  # Add the solution
                j = current[0][-1] + 1  # start a new game
                i = 0
                current = []
                occupied = []
                print("starting a new game")
                continue
            for elm in clear(i, j, N):  # mark all the occupied squares
                occupied.append(elm)
            i += 1
            j = 0
            print("Done marking occupied squares...")
            print(occupied[:-(len(clear(i, current[-1][-1], N)))])
            print("total occupied:")
            print(occupied)
            print("moving to next field")
            break
    # print("blax")
    if the_end == 1:
        break
    print("another round starts")

for i in solutions:
    print(i)
