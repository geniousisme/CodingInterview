class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        length = len(prices)
        max_profit  = 0
        if length == 0:
            return max_profit

        # assign dp table
        dp1 = [0 for i in xrange(length)]
        dp2 = [0 for i in xrange(length)]

        minV = prices[0]; maxV = prices[length - 1]

        # dp1[i]: the max profit you can have before i
        for i in xrange(1, length):
            minV = min(prices[i], minV)
            dp1[i] = max(dp1[i - 1], prices[i] - minV) # notice! dont make max as min...so stupid

        # dp2[i]: the max profit you can have after i
        for i in xrange(length - 2, -1, -1):
            maxV = max(prices[i], maxV)
            dp2[i] = max(dp2[i + 1], maxV - prices[i])

        # combine the result together and find the max value
        for i in xrange(length):
            if dp1[i] + dp2[i] > max_profit:
                max_profit = dp1[i] + dp2[i]
        return max_profit

