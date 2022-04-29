import pytest

from leetcode.k_radius_subarray_averages import Solution


@pytest.mark.parametrize('nums,k,ans', [
  ([7, 4, 3, 9, 1, 8, 5, 2, 6], 3, [-1, -1, -1, 5, 4, 4, -1, -1, -1]),
  ([100000], 0, [100000]),
  ([8], 100000, [-1]),
])
def test_k_avg(nums, k, ans):
  res = Solution.getAverages(nums, k)
  for i in range(0, len(res)):
    assert res[i] == ans[i]
