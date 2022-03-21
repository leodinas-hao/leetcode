'''
https://leetcode.com/problems/generate-parentheses/
https://github.com/azl397985856/leetcode/blob/master/problems/22.generate-parentheses.md


Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example 1:
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:
Input: n = 1
Output: ["()"]

Constraints:
1 <= n <= 8

Depth-first search (DFS) is an algorithm for traversing or searching tree or graph data structures.
The algorithm starts at the root node (selecting some arbitrary node as the root node in the case of a graph)
and explores as far as possible along each branch before backtracking
'''

from typing import List


class Solution:

  def __init__(self):
    self._list: List[str] = None
    self._num = 0

  def _dfs(self, left: int, right: int, parentheses: str):
    # stop if left < right
    if left > self._num or right > self._num or left < right:
      return
    if self._num == left == right:
      self._list.append(parentheses)
    # next left
    self._dfs(left + 1, right, parentheses + '(')
    # next right
    self._dfs(left, right + 1, parentheses + ')')

  def generate_parenthesis(self, n: int) -> List[str]:
    self._num = n
    self._list = []
    # start here
    self._dfs(0, 0, '')
    return self._list
