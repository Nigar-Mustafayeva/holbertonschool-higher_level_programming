#!/usr/bin/python3
"""
Pascal's Triangle module
"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing Pascal's triangle of n.
    
    Args:
        n (int): Number of rows of the triangle
    
    Returns:
        list: Pascal's triangle as a list of lists
    """
    if n <= 0:
        return []

    triangle = [[1]]  # first row

    for i in range(1, n):
        prev_row = triangle[i - 1]
        # Build the current row using previous row
        row = [1]  # first element
        for j in range(1, i):
            row.append(prev_row[j - 1] + prev_row[j])
        row.append(1)  # last element
        triangle.append(row)

    return triangle
