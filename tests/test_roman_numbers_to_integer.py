import pytest


from leetcode.roman_numbers_to_integer import Solution


@pytest.mark.parametrize('s,i', [
  ('XI', 11),
  ('IX', 9),
  ('XXVII', 27),
  ('MCMXCIV', 1994),
])
def test_roman_to_int(s, i):
  ans = Solution.roman_to_int(s)
  assert ans == i
