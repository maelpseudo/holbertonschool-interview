#!/usr/bin/python3

# Function to unlock boxes
def canUnlockAll(boxes):
    # isopen is a list that contains all open status of boxes
    isopen = []
    for i in range(len(boxes)):
        isopen.append(0)
    isopen[0] = 1
    # we search in all boxes to open the box contained in the actual box
    # if a box doesn't call other boxes, the opening stops, which return then false
    for box in boxes:
        for j in box:
            isopen[j] = 1
            break

    # here, we test if all boxes are opened, if yes, return True, if not, return False
    if 0 in isopen:
        return "False"
    else:
        return "True"
