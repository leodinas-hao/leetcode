import pytest


from leetcode.smallest_string_with_a_given_numeric_value import Solution


@pytest.mark.parametrize('n,k,expt', [
  (3, 27, 'aay'),
  (5, 73, 'aaszz'),
  (1, 1, 'a'),
])
def test_smallest_string(n, k, expt):
  result = Solution.get_smallest_string(n, k)
  assert result == expt
