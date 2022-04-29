'''
Valid anagram
https://leetcode.com/problems/valid-anagram/

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false

Constraints:
1 <= s.length, t.length <= 5 * 10^4
s and t consist of lowercase English letters
'''

from collections import Counter


class Solution:
  @staticmethod
  def isAnagram(s: str, t: str) -> bool:

    return Counter(s) == Counter(t)

  @staticmethod
  def isAnagram2(s: str, t: str) -> bool:

    if len(s) != len(t):
      return False

    # set a list to represent the count of each alphabates
    alphabates = [0] * 26

    # count each letter in s (++1)
    for i in s:
      alphabates[ord(i) - ord('a')] += 1

    # count each letter in t (--1)
    for j in t:
      alphabates[ord(j) - ord('a')] -= 1

    # counts of all alphabates should be back to 0
    return alphabates.count(0) == 26
