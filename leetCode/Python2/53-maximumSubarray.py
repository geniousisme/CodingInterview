class Solution(object):
    def maxSubArrayI(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        last_max = 0
        maximum  = -9999
        for i in xrange(len(nums)):
            last_max = max(last_max + nums[i], nums[i])
            maximum  = max(last_max, maximum)
        return maximum

    def maxSubArray(self, nums):
        last_sum = 0
        maximum  = -9999
        for i in xrange(len(nums)):
            if last_sum < 0:
                last_sum = 0
            last_sum += nums[i]
            maximum  = max(last_sum, maximum)
        return maximum

if __name__ == "__main__":
    s = Solution()
    print s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])