# Time:  O(n)
# Space: O(1)
#
# Given an array with n objects colored red, white or blue, sort them so that objects of the same color are adjacent, 
# with the colors in the order red, white and blue.
#
# Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.
#
# Note:
# You are not suppose to use the library's sort function for this problem.
#
# click to show follow up.
#
# Follow up:
# A rather straight forward solution is a two-pass algorithm using counting sort.
# First, iterate the array counting number of 0's, 1's, and 2's, 
# then overwrite array with total number of 0's, then 1's and followed by 2's.
#
# Could you come up with an one-pass algorithm using only constant space?
#


class Solution:
    # @param {integer[]} nums
    # @return {void} Do not return anything, modify nums in-place instead.
    def sortColors(self, nums): # two pointers solution
        '''
        TC: O(n)
        SC: O(1)
        '''
        length = len(nums)
        zero_idx = i = 0; two_idx = length - 1
        while i <= two_idx:
              if nums[i] == 0:
                 nums[zero_idx], nums[i] = nums[i], nums[zero_idx]
                 zero_idx += 1
                 i        += 1
              elif nums[i] == 2:
                   nums[two_idx], nums[i] = nums[i], nums[two_idx]
                   two_idx -= 1
              else: # nums[i] == 1:
                   i += 1

    def sortColorsI(self, nums): # counting sort solution
        '''
        TC: O(n)
        SC: O(n)
        '''
        count  = [0, 0, 0]
        length = len(nums)
        k      = 0
        for i in xrange(length):
            count[nums[i]] += 1
        j = 0
        while j < length:
            while count[k]:
                  count[k] -= 1
                  nums[j] = k
                  j += 1
            k += 1

if __name__ == '__main__':
   s = Solution()
   nums = [0, 0]
   s.sortColors(nums)
   print nums
   nums = [1, 2, 0]
   s.sortColors(nums)
   print nums
   nums = [1, 1, 2, 1, 0, 2, 2, 0, 1, 2, 0, 0, 1, 2]
   s.sortColors(nums)
   print nums