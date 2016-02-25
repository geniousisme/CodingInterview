class Solution:
    """
    @param nums: A list of integer which is 0, 1 or 2
    @return: nothing
    """
    class Solution(object):
    def sortColors(self, nums):
        colors = [0, 0, 0]
        length = len(nums)
        for i in xrange(length):
          colors[i] += 1
        ni = ci = 0
        while ni < length:
            while colors[ci] > 0:
                colors[ci] -= 1
                nums[ni] = ci
                ni += 1
            ci += 1

