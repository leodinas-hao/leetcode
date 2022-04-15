import pytest

from leetcode.convert_sorted_array_to_binary_search_tree import Solution, TreeNode


@pytest.mark.parametrize('nums', [
  [-10, -3, 0, 5, 9],
  [1, 3],
  [1, 2, 3, 4],
  [2, 4, 6],
])
def test_convert_sorted_array_to_bst(nums):
  bst = Solution().sorted_array_to_bst(nums)
  left = right = 0
  assert bst.val in nums

  def count_bst(node: TreeNode) -> int:
    if node is None:
      return 0

    assert node.val in nums
    return 1 + count_bst(node.left) + count_bst(node.right)

  left = count_bst(bst.left)
  right = count_bst(bst.right)
  assert abs(left - right) <= 1
  assert left + right + 1 == len(nums)
