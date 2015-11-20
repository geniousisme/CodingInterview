# You are a professional robber planning to rob houses along a street. 
# Each house has a certain amount of money stashed, the only constraint stopping you 
# from robbing each of them is that adjacent houses have security system connected
# and it will automatically contact the police if two adjacent houses were broken into on the same night.
#
# Given a list of non-negative integers representing the amount of money of each house, 
# determine the maximum amount of money you can rob tonight without alerting the police.


class Solution:
    '''
    TC: O(N)
    SC: O(N)
    '''
    # @param {integer[]} nums
    # @return {integer}
    def rob(self, nums):
        length = len(nums)
        if length == 0:
           return 0
        dp = [0, nums[0]]
        for i in xrange(2, length + 1):
            dp.append(max(dp[i - 1], dp[i - 2] + nums[i - 1]))
        return dp[-1]

class Solution2:
    '''
    TC: O(N)
    SC: O(1)
    '''
    def rob(self, num):
        if len(num) == 0:
            return 0
        if len(num) == 1:
            return num[0]
        num_i, num_i_1 = max(num[1], num[0]), num[0]
        for i in xrange(2, len(num)):
            num_i_1, num_i_2 = num_i, num_i_1
            num_i = max(num[i] + num_i_2, num_i_1);
        return num_i

if __name__ == '__main__':
   s = Solution()
   print s.rob([2, 1, 1, 2])
   print s.rob([3, 4])
   print s.rob([4, 5, 0, 6, 8])

