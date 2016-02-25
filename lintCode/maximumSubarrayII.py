class Solution:
    """
    @param nums: A list of integers
    @return: An integer denotes the sum of max two non-overlapping subarrays
    """
    def maxTwoSubArrays(self, nums):
        # reference: http://hehejun.blogspot.com/2015/01/lintcodemaximum-subarray-ii.html
        print nums
        length = len(nums)
        curr_max = -9999
        # notice, here we store global maximum
        # therefore, we should store very small value first
        # to avoid the full negative elements cases.
        left = [-9999 for i in xrange(length)]
        for i in xrange(length - 1):
            if curr_max < 0:
                curr_max = 0
            curr_max += nums[i]
            left[i + 1] = max(left[i], curr_max)
        # then, we combine local maximum for every position
        # and find the final maximum at the same time
        curr_max = final_max = -9999
        for i in xrange(length - 1, 0, -1):
            if curr_max < 0:
                curr_max = 0
            curr_max += nums[i]
            # if curr_max + left[i] > final_max:
            #     final_max = curr_max + left[i]
            final_max = max(curr_max + left[i], final_max)
        return final_max

if __name__ == "__main__":
    s = Solution()
    print s.maxTwoSubArrays([1, 3, -1, 2, -1, 2])
    # print s.maxTwoSubArrays([1, -99, -1, 2])
    # print s.maxTwoSubArrays([1, 2, 3, 4])
