#!/usr/bin/python3
"""Interview 0: lockboxes"""


def canUnlockAll(boxes):
    """Method that determines if all the boxes can be opened."""

    number_boxes = len(boxes)

    if boxes == []:
        return True

    boxes[0].append("opened")

    for boxe in boxes:
        index = boxes.index(boxe)
        for item in boxe:
            if (item != "opened" and item != index and item >= 0 and
                    item < number_boxes and "opened" not in boxes[item]):
                boxes[item].append("opened")

    for boxe in boxes:
        if "opened" not in boxe:
            return False
    return True
