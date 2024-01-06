#!/usr/bin/python3

def pascal_triangle(n):
  """
  Returns a list of lists of integers representing the Pascal's triangle of n.

  Args:
      n: An integer representing the number of rows in the triangle.

  Returns:
      A list of lists of integers representing the Pascal's triangle.
      Returns an empty list if n <= 0.
  """

  if n <= 0:
    return []

  triangle = [[1]]  # Initialize with the first row
  for i in range(1, n):
    row = [1]  # Start each row with 1
    for j in range(1, i):
      # Calculate values using the formula for Pascal's triangle
      value = triangle[i - 1][j - 1] + triangle[i - 1][j]
      row.append(value)
    row.append(1)  # End each row with 1
    triangle.append(row)

  return triangle
