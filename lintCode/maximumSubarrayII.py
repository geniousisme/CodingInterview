class Solution:
    """
    @param nums: A list of integers
    @return: An integer denotes the sum of max two non-overlapping subarrays
    """
    def maxTwoSubArrays(self, nums):
        min_idx = 0
        for i in xrange(len(nums)):
            if nums[i] < nums[min_idx]:
                min_idx = i
        if nums[min_idx] < 0:
            return self.maxSubarray(nums[:min_idx]) + self.maxSubarray(nums[min_idx + 1:])
        else:
            return self.maxSubarray(nums)

    def maxSubarray(self, nums):
        curr_max = final_max = -9999
        for n in nums:
            if curr_max < 0:
                curr_max = 0
            curr_max += n
            final_max = max(curr_max, final_max)
        return final_max

if __name__ == "__main__":
    s = Solution()
    print s.maxTwoSubArrays([1, 3, -1, 2, -1, 2])
    print s.maxTwoSubArrays([1, -99, -1, 2])
    print s.maxTwoSubArrays([1, 2, 3, 4])


