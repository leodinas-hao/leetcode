import pytest

from leetcode.unique_paths import Solution


@pytest.mark.parametrize('m,n,ans', [
  (3, 7, 28),
  (3, 2, 3),
])
def test_unique_paths(m, n, ans):
  res = Solution.unique_paths(m, n)
  assert res == ans
