from typing import List

import pytest

from leetcode.validate_binary_search_tree import Solution, TreeNode


def to_tree(nums: List[int]) -> TreeNode:
  '''convert number array to TreeNode'''

  count = len(nums)
  if list is None or count == 0:
    return None

  # create nodes
  nodes = [TreeNode(num) for num in nums]

  # build connections
  for i, node in enumerate(nodes):
    # left exits?
    i_left = i * 2 + 1
    if i_left < count and nodes[i_left].val is not None:
      node.left = nodes[i_left]

    # right exits?
    i_right = i * 2 + 2
    if i_right < count and nodes[i_right].val is not None:
      node.right = nodes[i_right]

  return nodes[0]


@pytest.mark.parametrize('nums,ans', [
  ([2, 1, 3], True),
  ([5, 1, 4, None, None, 3, 6], False),
  ([0], True),
  ([0, -1], True),
  ([5, 4, 6, None, None, 3, 7], False),
])
def test_validate_bst(nums, ans):
  res = Solution.isValidBST(to_tree(nums))
  assert res == ans
