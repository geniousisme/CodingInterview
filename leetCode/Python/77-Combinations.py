# Time:  O(n!)
# Space: O(n)
#
# Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.
# 
# For example,
# If n = 4 and k = 2, a solution is:
# 
# [
#   [2,4],
#   [3,4],
#   [2,3],
#   [1,2],
#   [1,3],
#   [1,4],
# ]
#

class Solution:
    # @param {integer} n
    # @param {integer} k
    # @return {integer[][]}
    def __init__(self):
        self.res  = []

    def combine(self, n, k):
        if self.res:
          self.res = []
        if not n:
           return self.res
        self.comb_helper([], range(1, n + 1), k)
        return self.res

    def comb_helper(self, comb, left_nums, k):
        if len(comb) == k:
            self.res.append(list(comb))
            return
        for i in xrange(len(left_nums)):
            comb.append(left_nums[i])
            self.comb_helper(comb, left_nums[i + 1:], k)
            comb.pop()


if __name__ == '__main__':
   s = Solution()
   combination = s.combine(4, 2)
   print combination
   print 'length:', len(combination)