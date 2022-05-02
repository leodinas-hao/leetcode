import pytest

from leetcode.evaluate_division import Solution


@pytest.mark.parametrize('equations,values,queries,ans', [
  (
    [["a", "b"], ["b", "c"]],
    [2.0, 3.0],
    [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]],
    [6.00000, 0.50000, -1.00000, 1.00000, -1.00000]
  ),
  (
    [["a", "b"], ["b", "c"], ["bc", "cd"]],
    [1.5, 2.5, 5.0],
    [["a", "c"], ["c", "b"], ["bc", "cd"], ["cd", "bc"]],
    [3.75000, 0.40000, 5.00000, 0.20000],
  ),
  (
    [["a", "b"]],
    [0.5],
    [["a", "b"], ["b", "a"], ["a", "c"], ["x", "y"]],
    [0.50000, 2.00000, -1.00000, -1.00000],
  ),
  (
    [["x1", "x2"], ["x2", "x3"], ["x3", "x4"], ["x4", "x5"]],
    [3.0, 4.0, 5.0, 6.0],
    [["x1", "x5"], ["x5", "x2"], ["x2", "x4"], ["x2", "x2"], ["x2", "x9"], ["x9", "x9"]],
    [360.00000, float(0.008333333333333333), 20.00000, 1.00000, -1.00000, -1.00000],
  ),
  (
      [["a", "b"], ["c", "d"]],
      [1.0, 1.0],
      [["a", "c"], ["b", "d"], ["b", "a"], ["d", "c"]],
      [-1.00000, -1.00000, 1.00000, 1.00000],
  ),
  (
    [["a", "b"], ["b", "c"], ["a", "e"], ["e", "c"]],
    [2.0, 2.0, 1.0, 4.0],
    [["a", "c"]],
    [4.00000]
  ),
])
def test_evaludate_division(equations, values, queries, ans):
  res = Solution.calcEquation(equations, values, queries)
  for i in range(len(ans)):
    assert res[i] == ans[i]
