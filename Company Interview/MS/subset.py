class Solution(object):
    def __init__(self):
        self.res = []
        self.length = 0

    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if self.res:
            self.res = []
        
        if nums:
            self.length = len(nums)
            nums.sort()
            self.subset_helper([], nums, 0)
        
        return self.res
    
    def subset_helper(self, sub, nums, start):
        self.res.append(sub)
        if len(sub) == self.length:
            return
        for i in xrange(start, self.length):
            self.subset_helper(sub + [nums[i]], nums, i + 1)

if __name__ == "__main__":
    s = Solution()
    print s.subsets([1, 2, 3])