'''
merge intervals
https://medium.com/javarevisited/top-25-amazon-sde-interview-questions-cfe0ef70ba9e
https://leetcode.com/problems/merge-intervals/

Given an array of intervals where intervals[i] = [start, end], merge all overlapping intervals,
and return an array of the non-overlapping intervals that cover all the intervals in the input.

Example 1:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

Example 2:
Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.

Constraints:
1 <= intervals.length <= 104
intervals[i].length == 2
0 <= start <= end <= 104
'''

from typing import List


class Solution:

  @staticmethod
  def merge(intervals: List[List[int]]) -> List[List[int]]:

    # sort the intervals based on the start value
    intervals.sort(key=lambda interval: interval[0])

    ans = []
    # add the 1st interval directly
    ans.append([intervals[0][0], intervals[0][1]])

    for _start, _end in intervals[1:]:
      last_end = ans[-1][1]

      if last_end < _start:
        # no overlapping, add to list
        ans.append([_start, _end])
      elif last_end >= _start and last_end <= _end:
        # overlapping with last, rewrite the last end
        ans[-1][1] = _end
      # else:
      #   # last_end > current end
      #   # overlapping, but no change required
      #   pass

    return ans
