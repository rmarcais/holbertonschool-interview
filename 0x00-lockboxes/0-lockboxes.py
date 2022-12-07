#!/usr/bin/python3
"""Interview 0: lockboxes"""


def canUnlockAll(boxes):
    """Method that determines if all the boxes can be unlocked."""

    if boxes == []:
        return True

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
        # We take the first key of boxes_to_unlock as index.
        index = boxes_to_unlock[0]

        # We check the keys of boxes[index]
        # to know if we can unlock antoher box.
        boxes_to_unlock = add_keys(boxes_to_unlock,
                                   unlocked_boxes, boxes, index)

        # We do this to mark the box at the index 'index' as unlocked.
        unlocked_boxes[index] = True

        # Once the box marked as unlocked,
        # we can remove its key from boxes_to_unlock.
        boxes_to_unlock.pop(0)

    # We return True if all boxes can be unlocked.
    return all(unlocked_boxes)


def add_keys(boxes_to_unlock, unlocked_boxes, boxes, index):
    """Method that adds keys to boxes_to_unlock"""
    for key in boxes[index]:
        # If boxes[key] is not marked as unlocked,
        # we add its key to boxes_to_unlock
        if key > 0 and key < len(boxes) and not unlocked_boxes[key]:
            boxes_to_unlock.append(key)
    return boxes_to_unlock
