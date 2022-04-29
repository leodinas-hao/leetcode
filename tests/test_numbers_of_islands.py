import pytest

from leetcode.numbers_of_islands import Solution


@pytest.mark.parametrize('grid, ans', [
  (
    [
      ["1", "1", "1", "1", "0"],
      ["1", "1", "0", "1", "0"],
      ["1", "1", "0", "0", "0"],
      ["0", "0", "0", "0", "0"]
    ],
    1
  ),
  (
    [
      ["1", "1", "0", "0", "0"],
      ["1", "1", "0", "0", "0"],
      ["0", "0", "1", "0", "0"],
      ["0", "0", "0", "1", "1"]
    ],
    3
  )
])
def test_numbers_of_islands(grid, ans):
  solution = Solution()
  res = solution.numIslands(grid)
  assert res == ans
