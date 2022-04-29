from typing import List

import pytest

from leetcode.merge_two_lists import ListNode, Solution


def make_list_node(nums: List[int]):
  cur = ListNode(nums[0])
  head = cur

  for i in range(1, len(nums)):
    cur.next = ListNode(nums[i])
    cur = cur.next

  return head


@pytest.mark.parametrize('l1,l2,ans', [
  ([1, 2, 4], [1, 3, 4], [1, 1, 2, 3, 4, 4]),
])
def test_merge_2_lists(l1, l2, ans):
  res = Solution.mergeTwoLists(make_list_node(l1), make_list_node(l2))

  for i in ans:
    assert i == res.val
    res = res.next
