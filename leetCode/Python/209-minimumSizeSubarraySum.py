# Time:  O(n)
# Space: O(1)
#
# Given an array of n positive integers and a positive integer s, 
# find the minimal length of a subarray of which the sum ≥ s. If there isn't one, return 0 instead.
#
# For example, given the array [2,3,1,2,4,3] and s = 7,
# the subarray [4,3] has the minimal length under the problem constraint.
#
# More practice:
# If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n).
#

# Sliding window solution.

class Solution:
    # @param {integer} s
    # @param {integer[]} nums
    # @return {integer}
    def minSubArrayLen(self, s, nums):
        start = end = sum = 0
        length = len(nums)
        min_length = length + 1
        
        while end < length:
              while end < length and sum < s:
                    sum += nums[end]
                    end += 1
              while start < end and sum >= s:
                    if sum >= s:
                       min_length = min(min_length, end - start)
                    sum -= nums[start]
                    start += 1
        return [0, min_length][min_length <= length]
    # Chris:TODO::need to implement the binary search way.
if __name__ == '__main__':
   s = Solution()
   print s.minSubArrayLen(7, [2,3,1,2,3,4])
   print s.minSubArrayLen(8, [2])
   print s.minSubArrayLen(3, [2, 3, 2])
   print s.minSubArrayLen(11, [1,2,3,4,5])
   




