class Solution(object):
    # def isMatch(self, s, p):
    #     m, n = len(s), len(p)
    #     dp = [[False]*(n+1) for _ in xrange(m+1)]
    #     dp[0][0] = True
    #
    #     for j in xrange(1, n+1):
    #         if p[j-1] != '*':
    #             break
    #         dp[0][j] = True
    #
    #     for j in xrange(1, n+1):
    #         for i in xrange(1, m + 1):
    #             if p[j-1] != '*':
    #                 dp[i][j] = dp[i-1][j-1] and (p[j-1] == s[i-1] or p[j-1] == '?')
    #             else:
    #                 dp[i][j] = dp[i-1][j] or dp[i][j-1]
    #     return dp[-1][-1]

    def isMatch(self, s, p):
        m, n = len(s), len(p)
        dp = [True] + [False] * m

        for j in xrange(1, n + 1):
            # dp2[0] = (dp[0] and p[j - 1] == '*')
            if p[j - 1] != '*':
                for i in reversed(xrange(1, m + 1)):
                    dp[i] = dp[i - 1] and (p[j - 1] == s[i - 1] or p[j - 1] == '?')
                dp[0] = (dp[0] and p[j - 1] == '*')
            else:
                for i in xrange(1, m + 1):
                    dp[i] = dp[i - 1] or dp[i]

        return dp[-1]


s = Solution()
assert s.isMatch('', '')
assert s.isMatch('a', '*')
assert s.isMatch('a', 'a')
assert not s.isMatch('aa', 'a')
assert not s.isMatch('ab', 'a')
assert not s.isMatch('a', 'ab')

assert s.isMatch('abca', 'ab?a')
assert s.isMatch('afcd', 'a*d')
assert not s.isMatch('aab', 'c*ab')

