#!/usr/bin/python3
"""lockbox solutions"""

def canUnlockAll(boxes):
    """
    Determines if all boxes can be opened using the available keys.
    Args:
        boxes: A list of lists, where each inner list represents the keys
               contained in a box.
    Returns:
        True if all boxes can be opened, False otherwise.
    """
    n = len(boxes)
    if n == 0:
        return False
    visited = [False] * n
    visited[0] = True  # The first box is unlocked
    keys_stack = boxes[0]
    while keys_stack:
        key = keys_stack.pop()
        if 0 <= key < n and not visited[key]:
            visited[key] = True
            keys_stack.extend(boxes[key])

    return all(visited)
