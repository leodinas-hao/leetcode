import pytest

from leetcode.prison_cells_after_n_days import Solution


@pytest.mark.parametrize('cells,n,ans', [
  ([0, 1, 0, 1, 1, 0, 0, 1], 7, [0, 0, 1, 1, 0, 0, 0, 0]),
  ([1, 0, 0, 1, 0, 0, 1, 0], 1000, [0, 0, 1, 1, 1, 1, 1, 0]),
])
def test_prison_cells_after_n_days(cells, n, ans):
  res = Solution.prison_after_n_days(cells, n)
  for i in range(0, len(res)):
    assert res[i] == ans[i]
