import pytest


from leetcode.parentheses import Solution


@pytest.mark.parametrize('num, expt', [
  (1, ['()']),
  (2, ['()()', '(())']),
])
def test_parentheses(num, expt):
  sol = Solution()
  result = sol.generateParenthesis(num)

  assert len(result) == len(expt)
  for s in result:
    assert s in expt
