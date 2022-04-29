'''
Validate binary search tree
https://leetcode.com/problems/validate-binary-search-tree/

Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:
The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

Example 1:
Input: root = [2,1,3]
Output: true

Example 2:
Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.

Constraints:
The number of nodes in the tree is in the range [1, 104].
-231 <= Node.val <= 231 - 1
'''

from typing import Optional


class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


class Solution:
  @staticmethod
  def isValidBST(root: Optional[TreeNode]) -> bool:
    def _check(node: TreeNode, left: int, right: int) -> bool:
      if node is None:
        return True

      if not (node.val < right and node.val > left):
        return False

      return _check(node.left, left, node.val) and _check(node.right, node.val, right)

    return _check(root, float('-inf'), float('inf'))