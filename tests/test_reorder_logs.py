import pytest

from leetcode.reorder_logs import Solution


@pytest.mark.parametrize('logs, ans', [
  (
    ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"],
    ["let1 art can", "let3 art zero", "let2 own kit dig", "dig1 8 1 5 1", "dig2 3 6"]
  )
])
def test_reorder_logs(logs, ans):
  res = Solution.orderLogs(logs)
  assert len(res) == len(ans)

  for i in range(0, len(res)):
    ans[i] == res[i]
