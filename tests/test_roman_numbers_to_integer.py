import pytest


from leetcode.roman_numbers_to_integer import Solution


@pytest.mark.parametrize('s,i', [
  ('XI', 11),
  ('IX', 9),
  ('XXVII', 27),
  ('MCMXCIV', 1994),
])
def test_roman_to_int(s, i):
  ans = Solution.roman2Int(s)
  assert ans == i


@pytest.mark.parametrize('i,s', [
  (11, 'XI'),
  (9, 'IX'),
  (27, 'XXVII'),
  (1994, 'MCMXCIV'),
])
def test_int_to_roman(i, s):
  ans = Solution.int2Roman(i)
  assert ans == s
