'''
Spiral Matrix II

https://medium.com/javarevisited/draft-100-days-challenge-to-cracking-the-coding-interview-c4de1e81fe1a
https://leetcode.com/problems/spiral-matrix-ii/

Given a positive integer n, generate a square matrix filled with elements from 1 to n² in spiral order.

Example 1:
Input: 3
Output:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]

Example 2:
Input: 4
Output:
[
 [ 1,   2,   3,   4 ],
 [ 12,  13,  14,  5 ],
 [ 11,  16,  15,  6 ],
 [ 10,  9,   8,   7 ]
]
'''

from typing import List


class Solution:

  @staticmethod
  def generate_matrix(n: int) -> List[List[int]]:

    # init matrix with 0
    matrix = [[0] * n for _ in range(n)]

    dir = [
      [0, 1],  # go right
      [1, 0],  # go down
      [0, -1],  # go left
      [-1, 0]  # to up
    ]
    dc = row = col = 0

    for i in range(n * n):
      matrix[row][col] = i + 1

      next_row = dir[dc][0] + row
      next_col = dir[dc][1] + col

      if next_row >= n or next_col >= n or matrix[next_row][next_col] != 0:
        # dc = dc + 1 if dc < 3 else 0
        dc = (dc + 1) % 4
        row += dir[dc][0]
        col += dir[dc][1]
      else:
        row = next_row
        col = next_col

    return matrix
