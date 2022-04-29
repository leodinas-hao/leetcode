import pytest

from leetcode.max_sum_sub_array import Solution


@pytest.mark.parametrize('nums,ans', [
  ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6),
  ([1], 1),
  ([5, 4, -1, 7, 8], 23),
])
def test_max_sum_sub_array(nums, ans):
  res = Solution.maxSubarray(nums)
  assert res == ans
