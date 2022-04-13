import pytest

from leetcode.escape_the_ghosts import Solution


@pytest.mark.parametrize('ghosts,target,ans', [
  ([[1, 0], [0, 3]], [0, 1], True),
  ([[1, 0]], [2, 0], False),
  ([[2, 0]], [1, 0], False),
])
def test_escape_ghosts(ghosts, target, ans):
  res = Solution.escape(ghosts, target)
  assert res == ans
