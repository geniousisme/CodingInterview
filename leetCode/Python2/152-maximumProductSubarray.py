class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        ex. [2,3,-2,4] => 6
        """
        maximum = 0
        if nums:
            curr_max = maximum = curr_min = nums[0]
            for i in xrange(1, len(nums)):
                tmp_max = curr_max * nums[i]
                tmp_min = curr_min * nums[i]
                curr_max = max(tmp_max, tmp_min, nums[i])
                curr_min = min(tmp_max, tmp_min, nums[i])
                maximum = max(maximum, curr_max)
        return maximum

if __name__ == "__main__":
    s = Solution()
    print s.maxProduct([2,3,-2,4])
