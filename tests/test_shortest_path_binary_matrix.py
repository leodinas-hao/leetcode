import pytest

from leetcode.shortest_path_binary_matrix import Solution


@pytest.mark.parametrize('grid,c', [
  ([[0, 1], [1, 0]], 2),
  ([[0, 0, 0], [1, 1, 0], [1, 1, 0]], 4),
  ([[1, 0, 0], [1, 1, 0], [1, 1, 0]], -1),
])
def test_shortest_path_binary_matrix(grid, c):
  ans = Solution.shortestPathBinaryMatrix(grid)
  assert ans == c
