class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [float("inf")] * (n + 1)
        i = 1
        while i * i <= n:
            dp[i * i] = 1
            i += 1
        i = 1
        while i <= n:
            j = 1
            while i + j * j <= n:
                dp[i + j * j] = min(dp[i] + 1, dp[i + j * j])
                j += 1
            i += 1
        return dp[n]

if __name__ == "__main__":
    s = Solution()
    print s.numSquares(12)