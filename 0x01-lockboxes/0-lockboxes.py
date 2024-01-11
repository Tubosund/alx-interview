#!/usr/bin/python3

def can_unlock_all(boxes):
    """
    Determines if all boxes can be opened using the available keys.

    Args:
        boxes: A list of lists, where each inner list represents the keys
               contained in a box.

    Returns:
        True if all boxes can be opened, False otherwise.
    """

    keys = {0}  # Start with the key for box 0
    opened_boxes = 0

    while keys:
        new_keys = set()
        for key in keys:
            if key < len(boxes):  # Check if key is valid for a box
                opened_boxes += 1
                new_keys |= set(boxes[key])  # Add keys found in the opened box
        keys = new_keys - keys  # Update keys with newly found, unused keys

    return opened_boxes == len(boxes)

