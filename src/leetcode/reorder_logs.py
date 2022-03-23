'''
Reorder Data Log Files

https://medium.com/javarevisited/day-40-reorder-data-log-files-40abfc9a98e0

You have an array of logs. Each log is a space-delimited string of words.
For each log, the first word in each log is an alphanumeric identifier. Then, either:
Each word after the identifier will consist only of lowercase letters, or;
Each word after the identifier will consist only of digits.
We will call these two varieties of logs letter-logs and digit-logs. It is guaranteed that each log has at least one word after its identifier.
Reorder the logs so that all of the letter-logs come before any digit-log.
The letter-logs are ordered lexicographically ignoring identifiers, with the identifier used in case of ties.
The digit-logs should be put in their original order.
Return the final order of the logs.

Example
Input: logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
Output: ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]
'''

from typing import List


class Solution:

  @staticmethod
  def order_logs(logs: List[str]) -> List[str]:

    letter_logs = []
    digit_logs = []

    for log in logs:
      if log[log.find(' ') + 1] < 'a':
        digit_logs.append(log)
      else:
        letter_logs.append(log)

    # sort letter logs
    def sort_key(log: str) -> str:
      [id, *words] = log.split()
      words.append(id)
      return ' '.join(words)

    letter_logs.sort(key=sort_key)

    return letter_logs + digit_logs
