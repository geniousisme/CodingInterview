class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        zero_idx = 0
        for i in xrange(len(nums)):
            if nums[i] != 0:
                self.swap(nums, zero_idx, i)
                zero_idx += 1

    def swap(self, nums, idx1, idx2):
        nums[idx1], nums[idx2] = nums[idx2], nums[idx1]

if __name__ == "__main__":
    s = Solution()
    s.moveZeroes([0, 1, 0, 2, 3])
    s.moveZeroes([1, 0, 0, 3, 4])
    s.moveZeroes([])



