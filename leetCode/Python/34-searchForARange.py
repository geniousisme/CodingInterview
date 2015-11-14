# Time:  O(logn)
# Space: O(1)
#
# Given a sorted array of integers, find the starting and ending position of a given target value.
# 
# Your algorithm's runtime complexity must be in the order of O(log n).
# 
# If the target is not found in the array, return [-1, -1].
# 
# For example,
# Given [5, 7, 7, 8, 8, 10] and target value 8,
# return [3, 4].
#

class Solution1:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return a list of length 2, [index1, index2]
    def searchRange(self, A, target):
        end = len(A)
        forward = backward = self.binarySearch(A, 0, end, target) # binary search, find the target first
        for i in xrange(forward + 1, end):
            if A[i] != target:
               break
            else:
               forward = i
        for i in xrange(backward - 1, -1, -1):
            if A[i] != target:
               break
            else:
               backward = i
        return [backward, forward]

    def binarySearch(self, A, start, end, target):
        if len(A[start:end]) == 1:
        # if end - start == 2:
            if A[0] == target:
               return start
            else:
               return -1
        mid = (start + end) / 2
        if A[mid] > target:
           return self.binarySearch(A, start, mid, target)
        elif A[mid] < target:
             return self.binarySearch(A, mid, end, target)
        else: # A[mid] == target
             return mid

class Solution(object):
    def searchRange(self, nums, target):
        if not nums:
            return [-1, -1]
        return [self.left_binary_search(nums, target), self.right_binary_search(nums, target)]

    def left_binary_search(self, nums, target):
        end = len(nums) - 1; start = 0
        while start + 1 < end:
            mid = start + (end - start) / 2
            if nums[mid] >= target:
                end = mid
            else:
                start = mid
        if nums[start] == target:
            return start
        if nums[end] == target:
            return end
        return -1

    def right_binary_search(self, nums, target):
        end = len(nums) - 1; start = 0
        while start + 1 < end:
            mid = start + (end - start) / 2
            if nums[mid] <= target:
                start = mid
            else:
                end = mid
        if nums[end] == target:
            return end
        if nums[start] == target:
            return start
        return -1

if __name__ == '__main__':
   s = Solution()
   A =  [5, 7, 7, 7, 7, 7, 8, 8, 9, 10]
   print s.searchRange(A, 10)
   print s.searchRange(A, 8)
   print s.searchRange(A, 7)
   print s.searchRange(A, 5)
   print s.searchRange(A, 1)
   print s.searchRange(A, 100)
   print s.searchRange([2, 2], 2)





