# Given an unsorted array nums, reorder it in-place
# such that nums[0] <= nums[1] >= nums[2] <= nums[3]....
# For example, given nums = [3, 5, 2, 1, 6, 4],
# one possible answer is [1, 6, 2, 5, 3, 4].

class Solution(object):
      def wiggle_sort(self, nums):
          for i in xrange(len(nums) - 1):
            if i % 2 == 0:
                if nums[i] > nums[i + 1]:
                    self.swap(nums, i, i + 1)
            else:
                if nums[i] < nums[i + 1]:
                    self.swap(nums, i, i + 1)
          return nums

      def swap(self, nums, idx1, idx2):
          nums[idx1], nums[idx2] = nums[idx2], nums[idx1]