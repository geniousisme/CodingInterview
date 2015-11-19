class Solution(object): # in-place swap solution
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        non_zero_ptr = 0
        for i in xrange(len(nums)):
            if nums[i] != 0:
                nums[i], nums[non_zero_ptr] = nums[non_zero_ptr], nums[i]
                non_zero_ptr += 1

class Solution2(object): # write nums solution
    def moveZeroes(self, nums):
        zero_start_ptr = 0
        for i in xrange(len(nums)):
            if nums[i]:
                nums[zero_start_ptr] = nums[i]
                zero_start_ptr += 1
        # write the zero to the array directly
        for i in xrange(zero_start_ptr, len(nums)):
            nums[i] = 0

if __name__ == "__main__":
    s = Solution2()
    nums = [1, 2, 0, 0, 3, 4, 0]
    s.moveZeroes(nums)
    print nums
    nums = [0, 0, 3, 0]
    s.moveZeroes(nums)
    print nums