class Solution:
    # @param nums: an integer[]
    # @return: an integer
    def maxProduct(self, nums):
        # write your code here
        curr_max = curr_min = 1
        final_max = -9999
        for n in nums:
            tmp_max = curr_max * n
            tmp_min = curr_min * n
            curr_max = max(tmp_max, tmp_min, n)
            curr_min = min(tmp_max, tmp_min, n)
            final_max = max(final_max, curr_max)
        return final_max
