class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_price = 9999
        max_profit = 0 # notice the situation of prices is []
        for price in prices:
            if price < min_price:
                min_price = price
            profit = price - min_price
            if profit > max_profit:
                max_profit = profit
        return max_profit

if __name__ == "__main__":
    s = Solution()
    print s.maxProfit()