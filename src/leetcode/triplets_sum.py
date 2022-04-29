'''
https://medium.com/javarevisited/100-days-to-amazon-day-1-b9e07228f079

Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0?
Find all unique triplets in the array which gives the sum of zero

'''

from typing import List


class Solution:
  @staticmethod
  def threeSum(arr: List[int]) -> List[List[int]]:
    target = 0
    ans = []  # for answer list
    ls: List[str] = []  # a string list for checking unique format: "a:b:c"

    arr.sort()  # sort ascending

    l = r = 0
    nums = len(arr)

    for i in range(0, nums - 2):
      l = i + 1    # pick from left
      r = nums - 1  # pick from right

      while l < r:
        if arr[i] + arr[l] + arr[r] == target:
          s = f'{arr[i]}:{arr[l]}:{arr[r]}'
          if s not in ls:
            ans.append([arr[i], arr[l], arr[r]])
            ls.append(s)
          l += 1
          r -= 1
        elif arr[i] + arr[l] + arr[r] > target:
          r -= 1
        else:
          l += 1

    return ans
