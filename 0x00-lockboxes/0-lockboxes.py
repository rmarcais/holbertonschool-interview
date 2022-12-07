#!/usr/bin/python3
"""Interview 0: lockboxes"""


def canUnlockAll(boxes):
    """Method that determines if all the boxes can be unlocked."""

    if boxes == []:
        return True

    boxes_to_unlock = [0]
    unlocked_boxes = [False for box in boxes]
    unlocked_boxes[0] = True

    while len(boxes_to_unlock) > 0:
        index = boxes_to_unlock[0]
        for key in boxes[index]:
            if (key < len(boxes) and not unlocked_boxes[key]
                    and key not in boxes_to_unlock):
                boxes_to_unlock.append(key)
        unlocked_boxes[index] = True
        boxes_to_unlock.pop(0)
    return all(unlocked_boxes)
