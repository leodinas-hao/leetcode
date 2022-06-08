'''
Shortest path in binary matrix
https://leetcode.com/problems/shortest-path-in-binary-matrix/

Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix. If there is no clear path, return -1.

A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:
All the visited cells of the path are 0.
All the adjacent cells of the path are 8-directionally connected (i.e., they are different and they share an edge or a corner).
The length of a clear path is the number of visited cells of this path.

Example 1:
0 1
 \
1 0
Input: grid = [[0,1],[1,0]]
Output: 2

Example 2:
0-0 0
   \
1 1 0
    |
1 1 0
Input: grid = [[0,0,0],[1,1,0],[1,1,0]]
Output: 4

Example 3:
1 0 0
1 1 0
1 1 0
Input: grid = [[1,0,0],[1,1,0],[1,1,0]]
Output: -1

Constraints:
n == grid.length
n == grid[i].length
1 <= n <= 100
grid[i][j] is 0 or 1
'''

from queue import Queue
from typing import List


class Solution:
  @staticmethod
  def shortestPathBinaryMatrix(grid: List[List[int]]) -> int:
    n = len(grid)

    if grid[0][0] == 1 or grid[n - 1][n - 1] == 1:
      return -1

    dirs = [
      (1, 1),  # down right
      (1, 0),  # down
      (0, 1),  # right
      (-1, 1),  # up right
      (1, -1),  # left
      (-1, 0),  # up
      (0, -1),  # left
      (-1, -1)  # up left
    ]

    queue = Queue()
    queue.put((0, 0, 1))
    while not queue.empty():
      (r, c, s) = queue.get()
      if r == n - 1 and c == n - 1:
        return s

      grid[r][c] = 1

      for (x, y) in dirs:
        x = r + x
        y = c + y
        if x >= 0 and y >= 0 and x < n and y < n and grid[x][y] == 0:
          queue.put((x, y, s + 1))
          grid[x][y] = 1

    return -1
