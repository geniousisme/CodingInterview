# Suppose a sorted array is rotated at some pivot unknown to you beforehand.
# (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
# You are given a target value to search.
# If found in the array return its index, otherwise return -1.
# You may assume no duplicate exists in the array.

class Solution(object):
    def search(self, nums, target):
        '''
        Time:  O(logn)
        Space: O(1)
        '''
        if not nums:
            return -1
        start = 0; end = len(nums) - 1
        while start + 1 < end:
            mid = (start + end) / 2
            if nums[mid] == target:
                return mid
            if nums[start] < nums[mid]:
                if nums[start] <= target <= nums[mid]: # notice the boundry condition!
                    end = mid
                else:
                    start = mid
            else:
                if nums[mid] <= target <= nums[end]:
                    start = mid
                else:
                    end = mid
        if nums[start] == target:
            return start
        if nums[end] == target:
            return end
        return -1

# Follow up for "Search in Rotated Sorted Array":
# What if duplicates are allowed?
# Would this affect the run-time complexity? How and why?
# Write a function to determine if a given target is in the array.

class Solution(object):
    def search(self, nums, target):
        '''
        Time:  O(n)
        Space: O(1)
        '''
        start = 0; end = len(nums) - 1
        while start + 1 < end:
            mid = (start + end) / 2
            if nums[mid] == target:
                return True
            if nums[start] == nums[mid]:
                start = start + 1
            elif nums[start] < nums[mid]:
                if nums[start] <= target <= nums[mid]:
                    end = mid
                else:
                    start = mid
            else:
                if nums[mid] <= target <= nums[end]:
                    start = mid
                else:
                    end = mid
        if nums[start] == target:
            return True
        if nums[end] == target:
            return True
        return False