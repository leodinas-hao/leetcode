'''
Number of Islands

https://medium.com/@akshay_ravindran/day-33-number-of-islands-80ecd0490fe3
https://leetcode.com/problems/number-of-islands/


Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
You may assume all four edges of the grid are all surrounded by water.

Example 1:
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3

Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.

'''

from typing import List


class Solution:

  def _dfs(self, grid: List[List[str]], x: int, y: int):
    '''depth first search to traverse the grid,
    change "1" to "0" to avoid double counting the island
    or return if outside of the edges
    '''

    if x < 0 or y < 0 or y >= len(grid) or x >= len(grid[y]) or grid[y][x] == '0':
      return

    grid[y][x] = '0'
    # traverse 4 directions
    self._dfs(grid, x + 1, y)
    self._dfs(grid, x - 1, y)
    self._dfs(grid, x, y + 1)
    self._dfs(grid, x, y - 1)

  def numIslands(self, grid: List[List[str]]) -> int:
    ans = 0

    for y in range(len(grid)):
      for x in range(len(grid[y])):
        if grid[y][x] == '1':
          ans += 1
          self._dfs(grid, x, y)

    return ans
