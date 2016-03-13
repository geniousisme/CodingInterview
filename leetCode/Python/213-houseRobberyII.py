# Time:  O(n)
# Space: O(1)
#
# Note: This is an extension of House Robber.
#
# After robbing those houses on that street, the thief has found himself a new place
# for his thievery so that he will not get too much attention. This time, all houses
# at this place are arranged in a circle. That means the first house is the neighbor
# of the last one. Meanwhile, the security system for these houses remain the same as
# for those in the previous street.
#
# Given a list of non-negative integers representing the amount of money of each house,
# determine the maximum amount of money you can rob tonight without alerting the police.
#

class Solution1:
    # @param {integer[]} nums
    # @return {integer}
    def rob(self, nums):
        if not nums:
           return 0
        return max(self.robLinear(nums[1:]), self.robLinear(nums[2:-1]) + nums[0])

    def robLinear(self, nums):
        if not nums:
           return 0
        dp = [0, nums[0]]
        for i in xrange(2, len(nums) + 1):
            dp.append(max(dp[i - 1], dp[i - 2] + nums[i - 1]))
        return dp[-1]

class Solution(object): # more beautiful code
    # @param {integer[]} nums
    # @return {integer}
    def rob(self, nums):
        if not nums:
           return 0
        if len(nums) == 1:
            return nums[0]
        # if you rob the first house, then you cannot rob the last house;
        # if you rob the last house, then you cannot rob the first house.
        return max(self.robLinear(nums[1:]), self.robLinear(nums[:-1]))

    def robLinear(self, nums):
        if not nums:
           return 0
        dp = [0, nums[0]]
        for i in xrange(2, len(nums) + 1):
            dp.append(max(dp[i - 1], dp[i - 2] + nums[i - 1]))
        return dp[-1]

if __name__ == '__main__':
   s = Solution()
   print s.rob([1, 2, 3, 4, 5])
   print s.rob([3, 2, 1])
   print s.rob([3, 6])
   print s.rob([])


   # print s.rob([4, 5, 0, 6, 8])
        