# Time:  O(n * 2^n)
# Space: O(1)
#
# Given a set of distinct integers, S, return all possible subsets.
#
# Note:
# Elements in a subset must be in non-descending order.
# The solution set must not contain duplicate subsets.
# For example,
# If S = [1,2,3], a solution is:
#
# [
#   [3],
#   [1],
#   [2],
#   [1,2,3],
#   [1,3],
#   [2,3],
#   [1,2],
#   []
# ]
#

class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def __init__(self):
        self.res = []
        self.length = 0 

    def subsets(self, nums):
        # nums.sort()
        self.length = len(nums)
        self.DFS([], 0, nums, 0)
        return self.res

    def DFS(self, comb, start, nums, depth): # optimized, use index but not whole list
        self.res.append(list(comb))
        if depth == self.length:  return
        for i in xrange(start, self.length):
            comb.append(nums[i])
            self.DFS(comb, i + 1, nums, depth + 1)
            comb.pop()

class Solution2(object):
    def subsets(self, S):
        result = []
        i, count = 0, 1 << len(S)
        S = sorted(S)

        while i < count:
            cur = []
            for j in xrange(len(S)):
                if i & 1 << j:
                    cur.append(S[j])
            result.append(cur)
            i += 1

        return result

if __name__ == '__main__':
   s = Solution()
   print s.subsets([1, 2, 3])