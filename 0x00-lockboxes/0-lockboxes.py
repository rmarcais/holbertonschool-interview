#!/usr/bin/python3
"""Interview 0: lockboxes"""


def canUnlockAll(boxes):
    """Method that determines if all the boxes can be unlocked."""

    number_boxes = len(boxes)

    if boxes == []:
        return True

    # The first box is unlocked
    unlocked_boxes = [0]

    for boxe in boxes:
        index = boxes.index(boxe)
        for key in boxe:
            # If the key can unlock a locked box of the list 'boxes',
            # we append "ul" to this box
            if (key != index and key >= 0 and
                    key < number_boxes and key not in unlocked_boxes):
                unlocked_boxes.append(key)

    print(unlocked_boxes)
    return len(unlocked_boxes) == number_boxes
