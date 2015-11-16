# Time:  O(n)
# Space: O(n)
#
# Given an array of integers and an integer k, return true if 
# and only if there are two distinct indices i and j in the array 
# such that nums[i] = nums[j] and the difference between i and j is at most k.
#

class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {boolean}
    def containsNearbyDuplicate(self, nums, k):
        numTable = {}
        for i in xrange(len(nums)):
            if numTable.get(nums[i]) is not None:
               if i - numTable[nums[i]] <= k:
                  return True
               else:
                  numTable[nums[i]] = i
            else:
               numTable[nums[i]] = i
        return False