'''
https://akshay-ravindran.medium.com/100-day-challenge-to-cracking-the-coding-interview-cef2a745b7c0

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
push(x) — Push element x onto stack.
pop() — Removes the element on top of the stack.
top() — Get the top element.
getMin() — Retrieve the minimum element in the stack.

MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.
'''

import sys


class MinStack:

  def __init__(self):
    self._nums = []
    # to keep track of ordered list with minimum numbers always at the end
    self._mins = []

  @property
  def min(self):
    return self._mins[-1] if self._mins else sys.maxsize

  def getMin(self):
    return self.min

  def push(self, i: int):
    self._nums.append(i)
    if i <= self.min:
      self._mins.append(i)

  def pop(self):
    i = self._nums.pop()
    if i == self.min:
      self._mins.pop()
    return i

  def top(self):
    return self._nums[-1]
