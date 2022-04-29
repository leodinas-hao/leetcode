import pytest

from leetcode.partition_labels import Solution


@pytest.mark.parametrize('s,expt', [
  ('ababcbacadefegdehijhklij', [9, 7, 8]),
  ('eccbbbbdec', [10]),
  ('abcd', [1, 1, 1, 1]),
])
def test_partition_lables(s, expt):
  result = Solution.partitionLabels(s)
  assert len(result) == len(expt)
  for i in range(0, len(result)):
    assert result[i] == expt[i]
