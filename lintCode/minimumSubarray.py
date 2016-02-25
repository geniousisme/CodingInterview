class Solution:
    """
    @param nums: a list of integers
    @return: A integer denote the sum of minimum subarray
    """
    def minSubArrayI(self, nums):
        # write your code here
        # dry run wrongly...damn it...
        curr_min = final_min = 9999
        for n in nums:
            curr_min  = min(curr_min + n, n)
            final_min = min(final_min, curr_min)
        return final_min

    def minSubArray(self, nums):
        # write your code here
        curr_min = final_min = 9999
        for n in nums:
            if curr_min > 0:
                curr_min = 0
            curr_min += n
            final_min = min(final_min, curr_min)
        return final_min

if __name__ == "__main__":
    s = Solution()
    print s.minSubArray([1, -1, -2, 1])


