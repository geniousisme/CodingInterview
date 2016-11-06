class Solution(object):
    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        self.solve(dp, 1, n)
        self.print_path(dp, 1, n)
        return dp[1][n]
 
    def solve(self, dp, L, R):
        if L >= R: 
            return 0
        if dp[L][R]: 
            return dp[L][R]
        print "L", L, "R", R
        options = [i + max(self.solve(dp, L, i - 1), self.solve(dp, i + 1, R)) for i in range(L, R + 1)]
        print options
        dp[L][R] = min(options)
        print "min options", dp[L][R]
        return dp[L][R]
 
    def print_path(self, dp, L, R):
        if L >= R: return
        for i in range(L, R + 1):
            if dp[L][R] == i + max(dp[L][i - 1], dp[i + 1][R]):
                print i
                if dp[L][i - 1] > dp[i + 1][R]:
                    self.print_path(dp, L, i - 1)
                else:
                    self.print_path(dp, i + 1, R)
                break

if __name__ == "__main__":
    s = Solution()
    # s.getMoneyAmount(1)
    # s.getMoneyAmount(2)
    s.getMoneyAmount(3)
    # s.getMoneyAmount(4)

