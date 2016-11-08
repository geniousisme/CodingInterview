# Suppose a sorted array is rotated at some pivot unknown to you beforehand.
# (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
# You are given a target value to search.
# If found in the array return its index, otherwise return -1.
# You may assume no duplicate exists in the array.
class Solution(object):
    '''
    Time:  O(logn)
    Space: O(1)
    '''
    def search(self, nums, target):
        if not nums:
            return -1
        start = 0; end = len(nums) - 1
        while start + 1 < end:
            mid = (start + end) / 2
            if nums[mid] == target:
                return mid
            elif nums[mid] >= nums[start]:
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
            return start
        if nums[end] == target:
            return end
        return -1

class Solution1(object):
    '''
    Time:  O(n)
    Space: O(1)
    '''
    def search(self, nums, target):
        length         = len(nums)
        pivot          = self.get_pivot(nums)
        if pivot < 0: # there is no pivot
          return self.binarySearch(nums, 0, length, target)
        else:
          post_idx  = self.binarySearch(nums[pivot + 1:], 0, length - pivot - 1, target) # search in previous list 
          prev_idx  = self.binarySearch(nums[:pivot + 1], 0, pivot + 1, target) # search in post list 
          if prev_idx > -1:
             return prev_idx
          elif post_idx > -1:
             return post_idx + pivot + 1
          else:
             return -1

    def get_pivot(self, nums):
        for i in xrange(1, len(nums)):
            if nums[i - 1] > nums[i]:
               return i - 1
        return -1

    def binarySearch(self, nums, start, end, target):
        if len(nums[start:end]) == 1:
           if nums[0] == target:
              return start
           else:
              return -1
        mid = (start + end) / 2
        if target > nums[mid]:
           return self.binarySearch(nums, mid, end, target)
        elif target < nums[mid]:
             return self.binarySearch(nums, start, mid, target)
        else:
             return mid

if __name__ == '__main__':
   s = Solution()
   print s.search([4, 5, 5, 6, 7, 0, 1, 2, 3, 3, 4], 5)
   print s.search([3, 1], 0)
   print s.search([1, 2, 3, 4, 5, 6, 7, 8], 5)
   

