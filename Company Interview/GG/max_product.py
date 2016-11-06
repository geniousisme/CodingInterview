class Solution(object):
    def max_product(self, target):
        if target == 3:
            return 2
        dp = [0, 1, 2]
        if target > 2:
            for num in xrange(3, target + 1):
                self.max_product_helper(dp, num)
        return dp[target]

    def max_product_helper(self, dp, num):
        dp.append(max([dp[i] * dp[num - i] for i in xrange(1, num / 2 + 1)] + [num]))

if __name__ == "__main__":
    s = Solution()
    print s.max_product(1)
    print s.max_product(2)
    print s.max_product(3)
    print s.max_product(5)
    print s.max_product(6)
    print s.max_product(7)

