import pytest

from leetcode.kth_largest import KthLargest


def test_kth_largest():
  kl = KthLargest(3, [4, 5, 8, 2])
  assert kl.add(3) == 4
  assert kl.add(5) == 5
  assert kl.add(10) == 5
  assert kl.add(9) == 8
  assert kl.add(4) == 8
