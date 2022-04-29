import pytest

from leetcode.alphabet_board_path import Solution


@pytest.mark.parametrize('target, ans', [
  ('leet', 'DDR!UURRR!!DDD!'),
  ('code', 'RR!DDRR!UUL!R!'),
])
def test_alphabet_board_path(target, ans):
  solution = Solution()
  res = solution.alphabetBoardPath(target)
  assert res == ans
