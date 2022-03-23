import pytest

from leetcode.min_stack import MinStack


def test_min_stack():
  stack = MinStack()
  stack.push(-2)
  stack.push(0)
  assert stack.min == -2
  stack.push(-3)
  assert stack.get_min() == -3
  stack.pop()
  assert stack.top() == 0
  assert stack.min == -2
