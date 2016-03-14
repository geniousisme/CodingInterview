class Solution(object):
    def sortColors(self, nums):
        if not nums:
            return nums
        zero_idx = i = 0; two_idx = len(nums) - 1
        while i <= two_idx: # notice! must be i <= two_idx
            if nums[i] == 0:
                nums[i], nums[zero_idx] = nums[zero_idx], nums[i]
                zero_idx += 1
                i += 1
            elif nums[i] == 2:
                nums[i], nums[two_idx] = nums[two_idx], nums[i]
                two_idx -= 1
            else:
                i += 1

if __name__ == '__main__':
   s = Solution()
   nums = [0, 0]
   s.sortColors(nums)
   print nums
   nums = [1, 2, 0] # this case can see why we need to let i <= two_idx
   s.sortColors(nums)
   print nums
   nums = [1, 1, 2, 1, 0, 2, 2, 0, 1, 2, 0, 0, 1, 2]
   s.sortColors(nums)
   print nums