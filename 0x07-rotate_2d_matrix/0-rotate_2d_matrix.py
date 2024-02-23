#!/usr/bin/python3
"""0-rotate_2d_matrix"""

def rotate_2d_matrix(matrix):
    """
    Rotates a 2D matrix by 90 degrees clockwise in-place.

    Args:
        matrix: A 2D list of integers representing the matrix to be rotated.

    Returns:
        None. The matrix is modified in-place.
    """

    n = len(matrix)
    # Transpose the matrix
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row of the transposed matrix
    for i in range(n):
        matrix[i] = matrix[i][::-1]
