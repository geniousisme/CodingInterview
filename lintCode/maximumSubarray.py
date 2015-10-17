class Solution:
    """
    @param nums: A list of integers
    @return: An integer denote the sum of maximum subarray
    """
    def maxSubArrayI(self, nums):
        # write your code here
        curr_max = final_max = -9999
        for n in nums:
            curr_max = max(curr_max + n, n)
            final_max = max(curr_max, final_max)
        return final_max

    def maxSubArray(self, nums):
        # write your code here
        curr_max = final_max = -9999
        for n in nums:
            if curr_max < 0:
                curr_max = 0
            curr_max += n
            final_max = max(curr_max, final_max)
        return final_max
