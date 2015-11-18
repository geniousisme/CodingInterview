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
        '''
        TC: O(n)
        SC: O(k)
        '''
        dequeue = []
        max_numbers = []
        for i in xrange(len(nums)):
            # since we want to use idx to maintain the window size with k length
            # we store the index to the array, but not the val
            while dequeue and nums[dequeue[-1]] <= nums[i]:
                # and we keep the first index of the dequeue as the current max
                # so compare with the last, if the last index val is smaller than current element
                # just pop out
                dequeue.pop()
            # now we can append the idx
            dequeue.append(i)
            # if the first index is already equal to i - k, which means it exceeds the k size
            # we need to pop it out
            if dequeue[0] == i - k:
                dequeue.pop(0)
            # if the i is bigger than k - 1, which mean we reach k size, start to put 0 index values
            # into the max_numbers
            if i >= k - 1:
                max_numbers.append(nums[dequeue[0]])
        return max_numbers


if __name__ == '__main__':
   s = Solution()
   print s.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3)
   # print s.maxSlidingWindow([1], 1)


