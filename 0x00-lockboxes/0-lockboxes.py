#!/usr/bin/python3
"""Interview 0: lockboxes"""


def canUnlockAll(boxes):
    """Method that determines if all the boxes can be unlocked."""

    number_boxes = len(boxes)

    if boxes == []:
        return True

    # We append "ul" (that stands for unlocked) to the boxe 0
    boxes[0].append("ul")

    for boxe in boxes:
        index = boxes.index(boxe)
        for key in boxe:
            # If the key can unlock a locked box of the list 'boxes',
            # we append "ul" to this box
            if (key != "ul" and key != index and key >= 0 and
                    key < number_boxes and "ul" not in boxes[key]):
                boxes[key].append("ul")

    # We return False if one of the boxes can't be unlocked
    for boxe in boxes:
        if "ul" not in boxe:
            return False
    return True
