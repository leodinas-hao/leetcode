import pytest

from leetcode.triplets_sum import Solution


@pytest.mark.parametrize('arr,ans', [
  ([-2, -1, 1, 0], [[-1, 0, 1]]),
  ([-2, -1, 1, 2, 3, -3, 0], [[-2, 0, 2], [-1, 0, 1], [-3, 0, 3], [-2, -1, 3], [-3, 1, 2]]),
])
def test_triplets_sum(arr, ans):
  res = Solution.threeSum(arr)
  assert len(res) == len(ans)
  for a in ans:
    assert a in res
