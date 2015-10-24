class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        lenth = len(prices)
        max_profit = 0
        for i in xrange(1, lenth):
            profit = prices[i] - prices[i - 1]
            if profit > 0:
                max_profit += profit
        return max_profit

if __name__ == "__main__":
    s = Solution()
    print s.maxProfit([4, 8, 10, 5, 7, 9])


