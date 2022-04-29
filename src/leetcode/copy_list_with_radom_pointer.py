'''
Copy List with Random Pointer
https://medium.com/@akshay_ravindran/day-32-copy-list-with-random-pointer-69be693fcb92
https://leetcode.com/problems/copy-list-with-random-pointer/


A linked list of length n is given such that each node contains an additional random pointer,
which could point to any node in the list, or null.

Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes,
where each new node has its value set to the value of its corresponding original node.
Both the next and random pointer of the new nodes should point to new nodes in the copied list
such that the pointers in the original list and copied list represent the same list state.
None of the pointers in the new list should point to nodes in the original list.

For example, if there are two nodes X and Y in the original list, where X.random --> Y,
then for the corresponding two nodes x and y in the copied list, x.random --> y.

Return the head of the copied linked list.

The linked list is represented in the input/output as a list of n nodes.
Each node is represented as a pair of [val, random_index] where:
val: an integer representing Node.val
random_index: the index of the node (range from 0 to n-1) that the random pointer points to,
or null if it does not point to any node.
Your code will only be given the head of the original linked list.

Example 1:
Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]

Example 2:
Input: head = [[1,1],[2,1]]
Output: [[1,1],[2,1]]

Example 3:
Input: head = [[3,null],[3,0],[3,null]]
Output: [[3,null],[3,0],[3,null]]

Constraints:
0 <= n <= 1000
-104 <= Node.val <= 104
Node.random is null or is pointing to some node in the linked list.
'''

from typing import Dict, Optional


class Node:
  def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
    self.val = int(x)
    self.next = next
    self.random = random


class Solution:

  hmap = {}

  def copyRadmonListR(self, head: Optional[Node]) -> Optional[Node]:
    '''recursively copy the node'''

    if head is None:
      return None

    if self.hmap.get(head):
      return self.hmap[head]

    copy = Node(head.val)

    self.hmap[head] = copy
    copy.next = self.copyRadmonListR(head.next)
    copy.random = self.copyRadmonListR(head.random)

    return copy

  def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
    '''iterate the old node to copy one by one
    with hashmap to ensure not duplicating the copied node
    '''

    if head is None:
      return None

    nmap: Dict[Node, Node] = {None: None}

    cur = head
    while cur:
      nmap[cur] = Node(cur.val)
      cur = cur.next

    cur = head
    while cur:
      node = nmap[cur]
      node.next = nmap[cur.next]
      node.random = nmap[cur.random]
      cur = cur.next

    return nmap[head]
