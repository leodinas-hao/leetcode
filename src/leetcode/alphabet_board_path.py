'''
Alphabet Board Path
https://leetcode.com/problems/alphabet-board-path/

On an alphabet board, we start at position (0, 0), corresponding to character board[0][0].
Here, board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"], as shown in the diagram below.

-------------
| a b c d e |
| f g h i j |
| k l m n o |
| p q r s t |
| u v w x y |
| z |
-----

We may make the following moves:
'U' moves our position up one row, if the position exists on the board;
'D' moves our position down one row, if the position exists on the board;
'L' moves our position left one column, if the position exists on the board;
'R' moves our position right one column, if the position exists on the board;
'!' adds the character board[r][c] at our current position (r, c) to the answer.
(Here, the only positions that exist on the board are positions with letters on them.)

Return a sequence of moves that makes our answer equal to target in the minimum number of moves.
You may return any path that does so.

Example 1:
Input: target = "leet"
Output: "DDR!UURRR!!DDD!"

Example 2:
Input: target = "code"
Output: "RR!DDRR!UUL!R!"

Constraints:
1 <= target.length <= 100
target consists only of English lowercase letters.
'''


class Solution:

  def __init__(self):
    self.map = {
      'a': (0, 0), 'b': (0, 1), 'c': (0, 2), 'd': (0, 3), 'e': (0, 4),
      'f': (1, 0), 'g': (1, 1), 'h': (1, 2), 'i': (1, 3), 'j': (1, 4),
      'k': (2, 0), 'l': (2, 1), 'm': (2, 2), 'n': (2, 3), 'o': (2, 4),
      'p': (3, 0), 'q': (3, 1), 'r': (3, 2), 's': (3, 3), 't': (3, 4),
      'u': (4, 0), 'v': (4, 1), 'w': (4, 2), 'x': (4, 3), 'y': (4, 4),
      'z': (5, 0),
    }

  def _move(self, begin: str, target: str) -> str:
    # convert alphabet to position coordinate
    _from = self.map[begin]
    _to = self.map[target]
    path = ''

    # U or D
    gap = _from[0] - _to[0]
    path += 'U' * gap if gap >= 0 else 'D' * (-gap)
    # L or R
    gap = _from[1] - _to[1]
    path += 'L' * gap if gap >= 0 else 'R' * (-gap)

    return path

  def alphabetBoardPath(self, target: str) -> str:
    path = ''
    _from = 'a'

    for _to in target:
      if _to == 'z' and _from != 'z':
        # handle the edge case of moving to 'z'
        path += self._move(_from, 'u')
        path += self._move('u', 'z')
      else:
        path += self._move(_from, _to)
      _from = _to
      path += '!'

    return path
