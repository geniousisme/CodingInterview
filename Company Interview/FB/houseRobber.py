#!/usr/bin/env python
# -*- coding: utf-8 -*-

# house robber leetcode， follow up ： 输出最后抢了哪几个房子。
class Solution(object):
    def rob(self, houses):
        '''
        Time:  O(n)
        Space: O(n)
        '''
        dp = [0, houses[0]]
        for i in xrange(2, len(houses) + 1):
            # compare the curr house wealth + previous previous result(dp[i - 2]) & previous result(dp[i - 1])
            dp.appen(max(houses[i - 1] + dp[i - 2], dp[i - 1]))
        return dp[-1]

class Solution1(object):
    def rob(self, houses):
        '''
        Time:  O(n)
        Space: O(1)
        '''
        if not houses:
            return 0
        prev_prev, prev = 0, houses[0]
        for i in xrange(2, len(houses) + 1):
            curr = max(houses[i - 1] + prev_prev, prev)
            prev_prev, prev = prev, curr
        return prev

class SolutionVarient(object): # print out the house you rob
    def rob(self, houses):
        '''
        Time:  O(n)
        Space: O(n)
        '''
        dp = [(0, ""), (houses[0], str(houses[0]))]
        for i in xrange(2, len(houses) + 1):
            dp.append(max((dp[i - 2][0] + houses[i - 1], dp[i - 2][1] + "->" + str(houses[i - 1])), dp[i - 1]))
        return dp[-1][1]

if __name__ == "__main__":
    sv = SolutionVarient()
    print sv.rob([2, 1, 1, 2])
    print sv.rob([3, 4])
    print sv.rob([4, 5, 0, 6, 8])
