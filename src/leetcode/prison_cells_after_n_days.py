'''
Prison Cells after N days
https://medium.com/@akshay_ravindran/day-31-prison-cells-after-n-days-6954ed481483
https://leetcode.com/problems/prison-cells-after-n-days/

There are 8 prison cells in a row, and each cell is either occupied or vacant.
Each day, whether the cell is occupied or vacant changes according to the following rules:
If a cell has two adjacent neighbors that are both occupied or both vacant, then the cell becomes occupied.
Otherwise, it becomes vacant.
(Note that because the prison is a row, the first and the last cells in the row can't have two adjacent neighbors.)
We describe the current state of the prison in the following way: cells[i] == 1 if the i-th cell is occupied, else cells[i] == 0.
Given the initial state of the prison, return the state of the prison after N days (and N such changes described above.)

Example 1:
Input: cells = [0,1,0,1,1,0,0,1], N = 7
Output: [0,0,1,1,0,0,0,0]
Explanation:
The following table summarizes the state of the prison on each day:
Day 0: [0, 1, 0, 1, 1, 0, 0, 1]
Day 1: [0, 1, 1, 0, 0, 0, 0, 0]
Day 2: [0, 0, 0, 0, 1, 1, 1, 0]
Day 3: [0, 1, 1, 0, 0, 1, 0, 0]
Day 4: [0, 0, 0, 0, 0, 1, 0, 0]
Day 5: [0, 1, 1, 1, 0, 1, 0, 0]
Day 6: [0, 0, 1, 0, 1, 1, 0, 0]
Day 7: [0, 0, 1, 1, 0, 0, 0, 0]

Example 2:
Input: cells = [1,0,0,1,0,0,1,0], n = 1000000000
Output: [0,0,1,1,1,1,1,0]

Constraints:
cells.length == 8
cells[i] is either 0 or 1.
1 <= n <= 109
'''

from typing import List


class Solution:

  @staticmethod
  def prisonAfterNDays(cells: List[int], n: int) -> List[int]:

    cellCount = len(cells)
    yesterday = cells
    today = []

    for _ in range(1, n + 1):
      # 1st cell always 0
      today = [0]

      for p in range(1, cellCount - 1):
        today.append(1 if yesterday[p - 1] + yesterday[p + 1] != 1 else 0)

      # last cell always 0
      today.append(0)

      yesterday = today

    return today
