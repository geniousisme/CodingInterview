# Time:  O(k * C(n, k))
# Space: O(k)
# 
# Given a collection of candidate numbers (C) and a target number (T), 
# find all unique combinations in C where the candidate numbers sums to T.
# 
# Each number in C may only be used once in the combination.
# 
# Note:
# All numbers (including target) will be positive integers.
# Elements in a combination (a1, a2, ... , ak) must be in non-descending order. (ie, a1 <= a2 <= ... <= ak).
# The solution set must not contain duplicate combinations.
# For example, given candidate set 10,1,2,7,6,1,5 and target 8, 
# A solution set is: 
# [1, 7] 
# [1, 2, 5] 
# [2, 6] 
# [1, 1, 6]
#

#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution1:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    
    def __init__(self):
        self.res    = []
        self.length = 0

    def combinationSum2(self, candidates, target):
        self.length = len(candidates)
        candidates.sort()
        self.DFS(target, candidates, [], 0)
        return self.res

    def DFS(self, diff, candidates, comb, start):
        if not diff and comb not in self.res: # diff == 0
           self.res.append(comb)
           return self.res
        else:
           for i in xrange(start, self.length):
               if candidates[i] > diff:
                  return
               else:
                  self.DFS(diff - candidates[i], candidates, comb + [candidates[i]], i + 1)

class Solution(object):
    def __init__(self):
        self.res = []
        self.target = 0
    def combinationSum2(self, candidates, target):
        self.length = len(candidates)
        self.target = target
        if candidates:
            self.combination_sum_helper(sorted(candidates), 0, [], 0)
        return self.res

    def combination_sum_helper(self, candidates, curr_sum, combination, start):
        if curr_sum == self.target:
            self.res.append(combination)
            return
        for i in xrange(start, self.length):
            if self.target < candidates[i]:
                break
            if i > start and candidates[i] == candidates[i - 1]:
                continue
            self.combination_sum_helper(candidates, curr_sum + candidates[i], combination + [candidates[i]], i + 1)

if __name__ == '__main__':
   s = Solution()
   candidates = [10,1,2,7,6,1,5] 
   target     = 8
   print s.combinationSum2(candidates, target)
   