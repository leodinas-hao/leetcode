'''
Maximum Sum Sub array
https://medium.com/@akshay_ravindran/100-days-challenge-to-cracking-the-coding-interview-fb3f955012e4

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example 1:
Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6

Example 2:
Input: nums = [1]
Output: 1

Example 3:
Input: nums = [5,4,-1,7,8]
Output: 23

Constraints:
1 <= nums.length <= 105
-104 <= nums[i] <= 104
'''

from typing import List


class Solution:

  @staticmethod
  def maxSubarray(nums: List[int]) -> int:
    curSum = nums[0]
    maxSum = nums[0]

    for num in nums[1:]:
      curSum = max(num, num + curSum)
      maxSum = max(maxSum, curSum)

    return maxSum
