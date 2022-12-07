#!/usr/bin/python3
"""Interview 0: lockboxes"""


def canUnlockAll(boxes):
    """Method that determines if all the boxes can be unlocked."""

    # When we get the key of a box, we put it in this list.
    boxes_to_unlock = []

    # This list contains the number of the boxes we can unlock.
    # At this moment, no box can be unlocked.
    unlocked_boxes = [False for box in boxes]

    # We add the keys contained in the box 0 to the list.
    boxes_to_unlock = add_keys(boxes_to_unlock, unlocked_boxes, boxes, 0)

    # This means the box 0 can be unlocked
    unlocked_boxes[0] = True

    # While we can unlock boxes...
    while len(boxes_to_unlock) > 0:
        index = boxes_to_unlock[0]
        boxes_to_unlock = add_keys(boxes_to_unlock, unlocked_boxes, boxes, index)
        boxes_to_unlock.pop(0)
        print(type(boxes_to_unlock))
        unlocked_boxes[index] = True
        print(unlocked_boxes)
    return all(unlocked_boxes)
    

def add_keys(boxes_to_unlock, unlocked_boxes, boxes, index):
    """Method that adds keys to boxes_to_unlock"""
    for key in boxes[index]:
        if boxes[key] not in unlocked_boxes:
            boxes_to_unlock.append(key)
    return boxes_to_unlock
