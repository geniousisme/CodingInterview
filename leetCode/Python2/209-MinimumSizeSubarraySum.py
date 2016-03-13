class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        start = end = summation = 0
        min_len = len(nums) + 1 # notice the minimum initial value!!
        while end < len(nums):
            while summation < s and end < len(nums):
                summation += nums[end]
                end += 1
            while summation >= s and start < end:
                min_len = min(min_len, end - start)
                summation -= nums[start]
                start += 1
        return min_len if min_len <= len(nums) else 0

if __name__ == "__main__":
    s = Solution()
    print s.minSubArrayLen(7, [2,3,1,2,4,3])