# Time:  O(logn)
# Space: O(1)
#
# A peak element is an element that is greater than its neighbors.
# 
# Given an input array where num[i] != num[i+1], find a peak element and return its index.
# 
# The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.
# 
# You may imagine that num[-1] = num[n] = -infinite.
# 
# For example, in array [1, 2, 3, 1], 3 is a peak element and your function should return the index number 2.
#
# Note:
# Your solution should be in logarithmic complexity.
#

class Solution1:
    # @param nums, an integer[]
    # @return an integer
    def findPeakElement(self, nums): # recursive
        # length = len(nums)
        # if length == 1: return 0
        return self.searchPeak(nums, 0, len(nums) - 1)

    def searchPeak(self, nums, start, end):
        if end == start:
           return start
        if end == start + 1:
           return start if nums[start] > nums[end] else end
        mid = (end + start) / 2
        if nums[mid] > nums[mid + 1]:
           return self.searchPeak(nums, start, mid)
        elif nums[mid] < nums[mid + 1]:
             return self.searchPeak(nums, mid, end)

class Solution(object):
    def findPeakElement(self, nums):
        start = 0; end = len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start) / 2
            if nums[mid] > nums[mid + 1]:
                end = mid
            else:
                start = mid
        return [start, end][nums[end] > nums[start]]


if __name__ == '__main__':
   s = Solution()
   print s.findPeakElement([1, 5, 2, 3, 4, 2, 1])
   print s.findPeakElement([2, 1])
   print s.findPeakElement([1])


