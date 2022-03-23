import pytest

from leetcode.most_common_word import Solution


@pytest.mark.parametrize('p, banned, ans', [
  ('Bob hit a ball, the hit BALL flew far after it was hit.', ['hit'], 'ball')
])
def test_most_common(p, banned, ans):
  s = Solution.most_common_word(p, banned)
  assert s == ans
