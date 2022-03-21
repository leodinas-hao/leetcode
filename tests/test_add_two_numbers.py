from typing import List

import pytest

from leetcode.add_two_numbers import ListNode, Solution


def make_list_node(nums: List[int]):
  cur = ListNode(nums[0])
  head = cur

  for i in range(1, len(nums)):
    cur.next = ListNode(nums[i])
    cur = cur.next

  return head


@pytest.mark.parametrize('l1,l2,expt', [
  ([2, 4, 3], [5, 6, 4], [7, 0, 8]),
  ([0], [0], [0]),
  ([9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9], [8, 9, 9, 9, 0, 0, 0, 1]),
])
def test_add_two_numbers(l1, l2, expt):
  solution = Solution()

  s = solution.add_2_lists(make_list_node(l1), make_list_node(l2))

  for i in range(0, len(expt)):
    assert expt[i] == s.val
    s = s.next
