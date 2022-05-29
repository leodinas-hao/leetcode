'''
n-queens
https://leetcode.com/problems/n-queens/

The n-queens puzzle is the problem of placing n queens on an n x n chessboard
such that no two queens attack each other.
Given an integer n, return all distinct solutions to the n-queens puzzle.
You may return the answer in any order.
Each solution contains a distinct board configuration of the n-queens' placement,
where 'Q' and '.' both indicate a queen and an empty space, respectively.
Note: The queen can be moved any number of unoccupied squares in a straight line vertically, horizontally, or diagonally

Example 1:
Input: n = 4
Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above

Example 2:
Input: n = 1
Output: [["Q"]]

Constraints:
1 <= n <= 9
'''

from typing import List


class Solution:

  EMPTY = '.'
  QUEEN = 'Q'

  def __init__(self):

    # keep a reference of board size
    self.size = 0

  def createBoard(self, n: int) -> List[List[bool]]:
    ''' creates a board with all empty spaces
    True indicating Queen taken the place, otherwise not
    '''
    self.size = n
    return [[False] * n for _ in range(n)]

  def printBoard(self, board: List[List[bool]]) -> List[str]:
    '''prints a board
    replace True with "Q" otherwise "." and join all cells of a row to string
    so the printed board is a string list
    '''
    printed = []
    for row in board:
      printed.append(''.join([self.QUEEN if cell else self.EMPTY for cell in row]))
    return printed

  def isSafe(self, board: List[List[bool]], r: int, c: int) -> bool:
    '''checks if given position (r)ow & (c)olumn is safe to place the queen
    in another word, there is no other queen at horizontal/vertical/diagonal directions
    '''

    for i in range(self.size):
      # horizontal or vertical
      if board[r][i] or board[i][c]:
        return False

      # diagonal: up/left -1&-1 || up/right-1&+1 || down/left +1&-1 || down/right +1&+1
      up = r - i - 1
      down = r + i + 1
      left = c - i - 1
      right = c + i + 1
      if up >= 0 and left >= 0 and board[up][left]:
        return False
      if up >= 0 and right < self.size and board[up][right]:
        return False
      if down < self.size and left >= 0 and board[down][left]:
        return False
      if down < self.size and right < self.size and board[down][right]:
        return False

    return True

  def solve(self, solutions, board, col):
    if col == self.size:
      solutions.append(self.printBoard(board))
    else:
      for row in range(self.size):
        if self.isSafe(board, row, col):
          board[row][col] = True
          self.solve(solutions, board, col + 1)
          board[row][col] = False

  def solveNQueens(self, n: int) -> List[List[str]]:
    solutions = []
    board = self.createBoard(n)
    self.solve(solutions, board, 0)
    return solutions
