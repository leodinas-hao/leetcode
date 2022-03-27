import pytest

from leetcode.spiral_matrix import Solution


@pytest.mark.parametrize('n,expt', [
  (1, [[1]]),
  (2, [[1, 2], [4, 3]]),
  (3, [[1, 2, 3], [8, 9, 4], [7, 6, 5]]),
  (4, [[1, 2, 3, 4], [12, 13, 14, 5], [11, 16, 15, 6], [10, 9, 8, 7]])
])
def test_spiral_matrix(n, expt):
  ans = Solution.generate_matrix(n)

  for r in range(n):
    for c in range(n):
      ans[r][c] = expt[r][c]
