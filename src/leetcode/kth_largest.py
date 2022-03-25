'''
Kth Largest Element in a Stream
https://medium.com/javarevisited/the-ultimate-guide-to-100-days-of-coding-challenge-e6eff0023f41
https://leetcode.com/problems/kth-largest-element-in-a-stream/

Design a class to find the kth largest element in a stream. 
Note that it is the kth largest element in the sorted order, not the kth distinct element.

Implement KthLargest class:
KthLargest(int k, int[] nums) Initializes the object with the integer k and the stream of integers nums.
int add(int val) Appends the integer val to the stream and returns the element representing the kth largest element in the stream.

Example:
Input
["KthLargest", "add", "add", "add", "add", "add"]
[[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
Output
[null, 4, 5, 5, 8, 8]

Explanation
KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]);
kthLargest.add(3);   // return 4
kthLargest.add(5);   // return 5
kthLargest.add(10);  // return 5
kthLargest.add(9);   // return 8
kthLargest.add(4);   // return 8

Constraints:
1 <= k <= 104
0 <= nums.length <= 104
-104 <= nums[i] <= 104
-104 <= val <= 104
At most 104 calls will be made to add.
It is guaranteed that there will be at least k elements in the array when you search for the kth element.

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

Approach: Heap
This problem is a perfect one to be solved with a heap, also known as a priority queue.

In short, a heap is a data structure that is capable of giving you the smallest (or largest) element (by some criteria) in constant time,
while also being able to add elements and remove the smallest (or largest) element in only logarithmic time.
Imagine if you wanted to replicate this functionality naively with an array.
To make sure we can find the smallest element in constant time, let's just keep our array sorted,
so that the last element is always the largest (or smallest, depending on if we're sorting in ascending or descending order).
Removing the largest/smallest element will take O(1) time as we are popping from the end of the array.
However, to add a new element, we first need to find where the element should be inserted and then insert it by shifting the array,
which requires O(n) time. Now, there are potential improvements to this approach, like using a deque for removals
and insertions and binary searching to find insertion points, but the point is that a heap makes it so we don't need to worry about any of that.

In summary, a heap:

Stores elements, and can find the smallest (min-heap) or largest (max-heap) element stored in O(1)O(1).
Can add elements and remove the smallest (min-heap) or largest (max-heap) element in O(\log(n))O(log(n)).
Can perform insertions and removals while always maintaining the first property.

Algorithm

In the constructor, create a min heap using the elements from nums. Then, pop from the heap until heap.length == k.

For every call to add():

First, push val into heap.
Next, check if heap.length > k. If so, pop from the heap.
Finally, return the smallest value from the heap, which we can get in O(1)O(1) time.

'''

from typing import List
import heapq


class KthLargest:

  def __init__(self, k: int, nums: List[int]):
    self.k = k
    self.heap = nums
    heapq.heapify(self.heap)

    while len(self.heap) > k:
      heapq.heappop(self.heap)

  def add(self, val: int) -> int:
    heapq.heappush(self.heap, val)
    if len(self.heap) > self.k:
      heapq.heappop(self.heap)
    return self.heap[0]
