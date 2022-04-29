import pytest

from leetcode.valid_anagram import Solution


@pytest.mark.parametrize('s,t,ans', [
  ('anagram', 'nagaram', True),
  ('rat', 'car', False),
])
def test_valid_anagram(s, t, ans):
  res = Solution.isAnagram(s, t)
  assert res == ans
