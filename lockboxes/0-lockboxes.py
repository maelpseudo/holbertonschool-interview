#!/usr/bin/python3
"""
0-lockboxes module:
Determines if all boxes can be unlocked starting from box 0,
given that each box may contain keys to other boxes.
"""


def canUnlockAll(boxes):
    """
    Determines if all boxes can be opened.

    Args:
        boxes (list of list of int):
            A list of n lists, where boxes[i] contains keys
            (integers) found in box i. A key k opens box k.
            Keys outside the range [0, n-1] are ignored.

    Returns:
        bool: True if every box from 0 to n-1 can be opened
              by collecting keys starting from box 0; False
              otherwise.
    """
    n = len(boxes)
    # Track which boxes have been opened (False = closed, True = open)
    opened = [False] * n
    opened[0] = True

    # Use a stack to process boxes that have been opened
    stack = [0]

    # Process until no more boxes to explore
    while stack:
        current = stack.pop()
        # For each key in the current box, try to open a new box
        for key in boxes[current]:
            if 0 <= key < n and not opened[key]:
                opened[key] = True
                stack.append(key)

    # Return True if all boxes are opened, False otherwise
    return all(opened)
