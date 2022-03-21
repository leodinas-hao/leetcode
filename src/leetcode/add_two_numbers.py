'''
https://leetcode.com/problems/add-two-numbers/
https://github.com/azl397985856/leetcode/blob/master/problems/2.add-two-numbers.md

You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Examples:

1).
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

2).
Input: l1 = [0], l2 = [0]
Output: [0]

3).
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]

Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.
'''

from typing import Optional


# Definition for singly-linked list.
class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next


class Solution:
  def add_2_lists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    '''
    :param l1 [ListNode]
    :param l2 [ListNode]
    :returns [ListNode]
    '''

    if l1 is None or l2 is None:
      return None

    # carry over number of sum
    carry = 0
    current = ListNode(0)
    head = current

    while l1 or l2 or carry != 0:
      _sum = carry
      if l1:
        _sum += l1.val
        l1 = l1.next
      if l2:
        _sum += l2.val
        l2 = l2.next

      if _sum < 10:
        current.val = _sum
        carry = 0
      else:
        current.val = _sum % 10
        carry = _sum // 10

      # move to next
      if l1 or l2 or carry != 0:
        current.next = ListNode(0)
        current = current.next

    return head
