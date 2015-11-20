# Time:  O(n * 2^n)
# Space: O(1)
#
# Given a collection of integers that might contain duplicates, S, return all possible subsets.
# 
# Note:
# Elements in a subset must be in non-descending order.
# The solution set must not contain duplicate subsets.
# For example,
# If S = [1,2,2], a solution is:
# 
# [
#   [2],
#   [1],
#   [1,2,2],
#   [2,2],
#   [1,2],
#   []
# ]
#

class Solution1(object):
    # @param {integer[]} nums
    # @return {integer[][]}
    def __init__(self):
        self.res = []
        self.length = 0

    def subsetsWithDup(self, nums):
        self.length = len(nums)
        nums.sort()
        if not self.length:
           return []
        self.DFS(nums, [], 0, 0)
        return self.res

    def DFS(self, nums, comb, start, depth):
        if comb not in self.res:
           self.res.append(list(comb))
        if depth == self.length:
           return
        for i in xrange(start, self.length):
            # comb.append(nums[i])
            self.DFS(nums, comb + [nums[i]], i + 1, depth + 1) # this is the fastest one, think it will use the mem to trade for time
            # self.DFS(nums, comb, i + 1, depth + 1)
            # comb.pop()

    def subsetsIter(self, nums):
        self.length = len(nums)
        nums.sort()
        if not self.length:
           return []
        self.DFS(nums, [], 0, 0)
        return self.res

class Solution(object):
    def __init__(self):
        self.length = 0
    def subsetsWithDup(self, nums):
        # write your code here
        res = []
        if nums:
            nums.sort() # notice it must be increasing order
            self.length = len(nums)
            self.subset_helper(nums, res, [], 0)
        return res

    def subset_helper(self, nums, res, subset, start):
        res.append(subset)
        for i in xrange(start, self.length):
            if i > start and nums[i] == nums[i - 1]:
                continue
            self.subset_helper(nums, res, subset + [nums[i]], i + 1) # notice it is i + 1, not start + 1

if __name__ == '__main__':
   s = Solution()
   nums = [1, 2, 2]
   print s.subsetsWithDup(nums)