#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution1(object):
    def __init__(self):
        self.res    = []
        self.length = 0

    def combinationSum(self, candidates, target):
        self.length = len(candidates)
        candidates.sort()
        self.DFS(target, candidates, [], 0)
        return self.res

    def DFS(self, diff, candidates, comb, start):
        if not diff: # diff == 0
           self.res.append(list(comb)) # version 2: since we use the address(generator) of list directly, change it to list now
           return self.res
        else:
           for i in xrange(start, self.length):
               if candidates[i] > diff:
                  break # or you can write 'return', both end the function and ship to next recursion
               else:
                  comb.append(candidates[i]) # version 2: use append to record the list, but it change the list directly, need to pop out the thing later, after close the recursion
                  self.DFS(diff - candidates[i], candidates, comb, i)
                  comb.pop() # version 2: recover the value of comb now, backtracking

class Solution2(object):
    def __init__(self):
        self.res = []
        self.target = 0
        self.length = 0

    def combinationSum(self, candidates, target):
        self.res = []
        if candidates:
            self.target = target
            self.length = len(candidates)
            # notice! must be sorted, otherwise hard to see the replicate
            candidates.sort()
            self.comb_sum_helper(candidates, [], 0, 0)
        return self.res

    def comb_sum_helper(self, candidates, comb, curr_sum, start):
        if curr_sum == self.target:
            self.res.append(comb)
            return
        for i in xrange(start, self.length):
            if self.target - curr_sum < candidates[i]:
            # this condition must exist, we use it to
            # escape the infinite looping condition
                break
            self.comb_sum_helper(candidates, comb + [candidates[i]], curr_sum + candidates[i], i)

class Solution(object):
    def combinationSum(self, candidates, target):
        """
        Time:  O(k * n ^ k)
        Space: O(k)
        """
        def comb_sum_helper(comb, curr_sum, start):
            if curr_sum == target:
                res.append(comb)
                return
            if curr_sum > target:
                return
            for i in xrange(start, len(candidates)):
                comb_sum_helper(comb + [candidates[i]], curr_sum + candidates[i], i)

        res = []; length = len(candidates)
        if candidates:
            candidates = sorted(candidates)
            comb_sum_helper([], 0, 0)
        return res

if __name__ == '__main__':
   s = Solution()
   candidates = [3,6,7,2]
   target     = 7
   print s.combinationSum(candidates, target)