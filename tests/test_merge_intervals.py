import pytest

from leetcode.merge_intervals import Solution


@pytest.mark.parametrize('intervals, ans', [
  ([[1, 4], [4, 5]], [[1, 5]]),
  ([[1, 3], [2, 6], [8, 10], [15, 18]], [[1, 6], [8, 10], [15, 18]]),
  ([[6, 10], [4, 7], [15, 17], [16, 20], [1, 5]], [[1, 10], [15, 20]])
])
def test_merge_intervals(intervals, ans):
  res = Solution.merge(intervals)
  for i, interval in enumerate(res):
    assert ans[i][0] == interval[0]
    assert ans[i][1] == interval[1]
