import pytest

from leetcode.unique_paths import Solution


@pytest.mark.parametrize('m,n,ans', [
  (3, 7, 28),
  (3, 2, 3),
])
def test_unique_paths(m, n, ans):
  res = Solution.uniquePaths(m, n)
  assert res == ans


@pytest.mark.parametrize('m,n,ans', [
  (3, 7, 28),
  (3, 2, 3),
])
def test_unique_paths_dp(m, n, ans):
  res = Solution.uniquePathsDP(m, n)
  assert res == ans
