class Solution(object):
    def findValleyOrPeak(self, nums):
        if not nums:
            return None
        if len(nums) == 1:
            return nums[0]
        if nums[0] > nums[1]: # valley
            idx = (len(nums) + nums[0] - nums[-1]) / 2
        else: # peak
            idx = (len(nums) + nums[-1] - nums[0]) / 2
        return nums[idx]

if __name__ == "__main__":
    s = Solution()
    print s.findValleyOrPeak([1, 2, 3, 4, 3, 2])
    print s.findValleyOrPeak([4, 3, 2, 1, 2])
    print s.findValleyOrPeak([2, 3, 2, 1, 0])
    print s.findValleyOrPeak([3, 2, 1, 0, 1, 2, 3, 4])


