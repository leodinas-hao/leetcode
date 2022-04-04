import pytest

from leetcode.k_cloest_points_to_origin import Solution


@pytest.mark.parametrize('points, k, ans', [
  ([[1, 3], [-2, 2]], 1, [[-2, 2]]),
  ([[3, 3], [5, -1], [-2, 4]], 2, [[3, 3], [-2, 4]])
])
def test_k_cloest_points_to_origin(points, k, ans):
  res = Solution.k_closest(points, k)
  assert len(res) == k

  for r in res:
    assert r in ans
