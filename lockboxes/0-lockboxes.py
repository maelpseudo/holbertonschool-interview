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
            A list of n lists, where boxes[i] contains keys (integers) found in box i.
            A key k opens box k. Keys outside the range [0, n-1] are ignored.
    Returns:
        bool:
            True if every box from 0 to n-1 can be opened by collecting keys
            starting from box 0; False otherwise.
    """
    # Initialize open status: 0 = closed, 1 = open
    isopen = [0] * len(boxes)
    # Box 0 is unlocked by default
    isopen[0] = 1

    # Collect keys: for each box, mark the box corresponding to the first valid key as open
    for box in boxes:
        for key in box:
            # Only process keys that refer to existing boxes
            if 0 <= key < len(boxes):
                isopen[key] = 1
            # Break after first key, as in original logic
            break

    # Check final state: return True if no box remains closed
    return False if 0 in isopen else True
