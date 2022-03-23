'''
https://blog.devgenius.io/day-4-most-common-word-699675d81cc5

Given a paragraph and a list of banned words, return the most frequent word that is not in the list of banned words.
It is guaranteed there is at least one word that isn't banned, and that the answer is unique.
Words in the list of banned words are given in lowercase, and free of punctuation. Words in the paragraph are not case sensitive.
The answer is in lowercase.

Example:
Input:
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
Output: "ball"
Explanation:
"hit" occurs 3 times, but it is a banned word.
"ball" occurs twice (and no other word does), so it is the most frequent non-banned word in the paragraph.
Note that words in the paragraph are not case sensitive,
that punctuation is ignored (even if adjacent to words, such as "ball,"),
and that "hit" isn't the answer even though it occurs more because it is banned.
'''


from typing import List
import re


class Solution:
  @staticmethod
  def most_common_word(paragraph: str, banned: List[str]) -> str:

    all_words = re.findall(r'\w+', paragraph.lower())
    # filter banned ones & remove duplicate
    words = list(dict.fromkeys([word for word in all_words if word not in banned]))

    max = 0
    most = None
    for word in words:
      count = all_words.count(word)
      if count > max:
        most = word
        max = count

    return most
