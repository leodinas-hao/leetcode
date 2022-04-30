import pytest

from leetcode.minimum_absolute_sum_difference import Solution


@pytest.mark.parametrize('nums1,nums2,ans', [
  ([1, 7, 5], [2, 3, 5], 3),
  ([2, 4, 6, 8, 10], [2, 4, 6, 8, 10], 0),
  ([1, 10, 4, 4, 2, 7], [9, 3, 5, 1, 7, 4], 20),
  ([100, 95, 50], [50, 40, 0], 105)
])
def test_minimum_absolute_sum_difference(nums1, nums2, ans):
  res = Solution.minAbsoluteSumDiff(nums1, nums2)
  assert res == ans
