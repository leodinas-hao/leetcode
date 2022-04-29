import pytest

from leetcode.container_with_most_water import Solution


@pytest.mark.parametrize('height,ans', [
  ([1, 8, 6, 2, 5, 4, 8, 3, 7], 49),
  ([1, 1], 1),
  ([1, 2, 4, 3], 4)
])
def test_container_with_most_water(height, ans):
  res = Solution.maxArea(height)
  assert ans == res
