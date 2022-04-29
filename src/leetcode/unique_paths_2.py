'''
Unique Paths II
https://leetcode.com/problems/unique-paths-ii/

You are given an m x n integer array grid. There is a robot initially located at the top-left corner (i.e., grid[0][0]).
The robot tries to move to the bottom-right corner (i.e., grid[m-1][n-1]).
The robot can only move either down or right at any point in time.
An obstacle and space are marked as 1 or 0 respectively in grid. A path that the robot takes cannot include any square that is an obstacle.
Return the number of possible unique paths that the robot can take to reach the bottom-right corner.
The testcases are generated so that the answer will be less than or equal to 2 * 10^9.

Example 1:
Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
Output: 2
Explanation: There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right

Example 2:
Input: obstacleGrid = [[0,1],[0,0]]
Output: 1

Constraints:
m == obstacleGrid.length
n == obstacleGrid[i].length
1 <= m, n <= 100
obstacleGrid[i][j] is 0 or 1.
'''

from typing import List


class Solution:
  @staticmethod
  def uniquePaths(grid: List[List[int]]) -> int:

    # edge case if grid[0][0] is obstacled, then return 0
    if grid[0][0] == 1:
      return 0

    for i in range(len(grid)):
      for j in range(len(grid[i])):
        if i == 0 and j == 0:
          # mark origin point as 1
          grid[i][j] = 1
        else:
          # if obstacled, then set 0
          if grid[i][j] == 1:
            grid[i][j] = 0
          else:
            if i == 0 and j > 0:
              # first row, always be the previous cell value
              grid[i][j] = grid[i][j - 1]
            elif j == 0 and i > 0:
              # first column, always be the above cell value
              grid[i][j] = grid[i - 1][j]
            else:
              # cells in middle, always be above + previous cell values
              grid[i][j] = grid[i - 1][j] + grid[i][j - 1]

    return grid[-1][-1]
