class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        while i < len(nums):
            if nums[i] > 0 and nums[i] - 1 < len(nums) and nums[nums[i] - 1] != nums[i]:
                self.swap(nums, nums[i] - 1, i)
            else:
                i += 1
            # print nums

        for i in xrange(len(nums)):
            if nums[i] != i + 1:
                return i + 1
        return len(nums) + 1

    def swap(self, nums, idx1, idx2):
        nums[idx1], nums[idx2] = nums[idx2], nums[idx1]

if __name__ == "__main__":
    s = Solution()
    print s.firstMissingPositive([3, 4, 1, -1])