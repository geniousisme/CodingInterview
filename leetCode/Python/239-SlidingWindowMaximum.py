# Time:  O(n)
# Space: O(k)
#
# Given an array nums, there is a sliding window of size k
# which is moving from the very left of the array to the
# very right. You can only see the k numbers in the window.
# Each time the sliding window moves right by one position.
#
# For example,
# Given nums = [1,3,-1,-3,5,3,6,7], and k = 3.
#
# Window position                Max
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7
# Therefore, return the max sliding window as [3,3,5,5,6,7].
#
# Note:
# You may assume k is always valid, ie: 1 <= k <= input array's size for non-empty array.
#
# Follow up:
# Could you solve it in linear time?
#

import heapq

class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {integer[]}
    def maxSlidingWindowWithMaxFunc(self, nums, k):
        res = []
        if nums:
           for i in xrange(len(nums) - k + 1):
               res.append(max(nums[i:i + k]))
        return res

    def maxSlidingWindowWithHeap(self, nums, k):
        res = []
        if nums:
           for i in xrange(len(nums) - k + 1):
               tmp = nums[i:i + k]
               # print tmp
               heapq.heapify(tmp)
               # print 'after:', tmp
               res.append(tmp[-1])
        return res

    def maxSlidingWindow(self, nums, k):
        dequeue = []
        max_numbers = []
        for i in xrange(len(nums)):
            while dequeue and nums[dequeue[-1]] <= nums[i]:
                dequeue.pop()
            dequeue.append(i)
            if dequeue[0] == i - k:
                dequeue.pop(0)
            if i >= k - 1:
                max_numbers.append(nums[dequeue[0]])
        return max_numbers


if __name__ == '__main__':
   s = Solution()
   print s.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3)
   # print s.maxSlidingWindow([1], 1)


