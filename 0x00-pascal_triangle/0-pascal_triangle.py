#!/usr/bin/python3
"""
function that returns a list of intergers representing the 
pascal triangle of n:
"""

def pascal_triangle(n):
    """Creates list of integers in a Pascal triangle of a given integer"""

    if n <= 0:
        return []
    triangle = []
    for i in range(n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)
        triangle.append(row)
    return triangle
