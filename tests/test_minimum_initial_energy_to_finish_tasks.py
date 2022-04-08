import pytest

from leetcode.minimum_initial_energy_to_finish_tasks import Solution


@pytest.mark.parametrize('tasks,ans', [
  ([[1, 2], [2, 4], [4, 8]], 8),
  ([[1, 3], [2, 4], [10, 11], [10, 12], [8, 9]], 32),
  ([[1, 7], [2, 8], [3, 9], [4, 10], [5, 11], [6, 12]], 27),
])
def test_minimum_energy(tasks, ans):
  res = Solution.minimum_effort(tasks)
  assert res == ans
