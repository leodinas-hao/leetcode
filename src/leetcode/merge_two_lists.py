'''
https://medium.com/javarevisited/day-2-merge-two-sorted-list-130c7a0af86d

Merge two sorted linked lists and return it as a new list.
The new list should be made by splicing together the nodes of the first two lists.

Example:
Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
'''


# Definition for singly-linked list.
class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next


class Solution:
  @staticmethod
  def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
    head = ListNode(0)  # dummy head
    _node = head

    while l1 or l2:
      # check if a list ends
      if l1 is None or l2 is None:
        _node.next = l1 if l2 is None else l2
        break

      if l1.val <= l2.val:
        _node.next = l1
        l1 = l1.next
      else:
        _node.next = l2
        l2 = l2.next

      _node = _node.next

    return head.next
