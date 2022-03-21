import pytest

from leetcode.longest_substring import Solution


@pytest.mark.parametrize('s,len', [
  ['abcabcbb', 3],
  ['bbbbb', 1],
  ['pwwkew', 3],
  ['assdesstd', 3]
])
def test_longest_substring(s, len):
  result = Solution.length_of_longest_substring(s)
  assert result == len
