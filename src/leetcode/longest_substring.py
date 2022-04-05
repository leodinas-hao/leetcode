'''
Longest Substring Without Repeating Characters

https://leetcode.com/problems/longest-substring-without-repeating-characters/
https://github.com/azl397985856/leetcode/blob/master/problems/3.longest-substring-without-repeating-characters.md

Given a string s, find the length of the longest substring without repeating characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Constraints:
0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
'''

from collections import defaultdict
from typing import Dict


class Solution:

  @staticmethod
  def length_of_longest_substring_2(s: str) -> int:
    if len(s) < 2:
      return len(s)

    longest = 1
    substr = s[0]

    for c in s[1:]:
      pos = substr.find(c)
      if pos > -1:
        # found matching
        # update substr by removing everything prior the match char & suffix with the char at the end
        substr = substr[pos + 1:] + c
      else:
        # add new char to substr
        substr += c

      longest = max(longest, len(substr))

    return longest

  @staticmethod
  def length_of_longest_substring(s: str) -> int:
    longest = 0
    pos = 0
    char_pos: Dict[str, int] = defaultdict(lambda: 0)  # to avoid key error

    for i in range(len(s)):
      while char_pos[s[i]] != 0:
        char_pos[s[pos]] -= 1
        pos += 1
      char_pos[s[i]] += 1
      longest = max(longest, i - pos + 1)

    return longest
