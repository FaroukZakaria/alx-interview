#!/usr/bin/python3
"""
Checking if all boxes can be opened by keys inside each
"""


def canUnlockAll(boxes):
    """
    Returns True if all boxes given can be opened with given keys in each box
    """
    obtained_keys = set(boxes[0])
    filter(obtained_keys, boxes)

    while (len(obtained_keys) + 1 < len(boxes)):
        temp = set(obtained_keys)
        for key in temp:
            obtained_keys.update(boxes[key])
        filter(obtained_keys, boxes)
        if len(temp) == len(obtained_keys):
            """
            If after opening all boxes with given keys,
            no more obtained keys, then I'm stuck in a loop,
            and hence, I can't unlock them all
            """
            return False

    return True


def filter(set_list, goal_list):
    """
    Filter keys so only relevant ones remain
    """
    temp = set(set_list)
    for key in temp:
        if (key >= len(goal_list) or key == 0):
            set_list.remove(key)
