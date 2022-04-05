import pytest

from leetcode.unique_paths_2 import Solution


@pytest.mark.parametrize('grid, ans', [
  ([[0, 0, 0], [0, 1, 0], [0, 0, 0]], 2),
  ([[0, 1], [0, 0]], 1)
])
def test_unique_paths_2(grid, ans):
  res = Solution.unique_paths(grid)
  assert res == ans
