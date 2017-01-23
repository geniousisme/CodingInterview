class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        m, n = len(s), len(p)
        dp = [[False] * (n+1) for _ in xrange(m+1)]

        dp[0][0] = True
        for j in xrange(2, n+1):
            dp[0][j] = p[j-1] == '*' and dp[0][j-2]

        for i in xrange(1, m+1):
            for j in xrange(1, n+1):
                if p[j-1] != '*':
                    dp[i][j] = dp[i-1][j-1] and (s[i-1] == p[j-1] or p[j-1] == '.')
                else:
                    if p[j-2] == s[i-1] or p[j-2] == '.':
                        dp[i][j] = dp[i][j-2] or dp[i][j-1] or dp[i-1][j]
                    else:
                        dp[i][j] = dp[i][j-2]

        return dp[-1][-1]




s = Solution()
assert s.isMatch('', '')
assert s.isMatch('', 'a*n*p*')
assert not s.isMatch('', 'a*np*p*')
assert s.isMatch('a', 'a')
assert s.isMatch('a', '.')
assert s.isMatch('aaaa', 'a*')
assert not s.isMatch('aaab', 'a*')
assert s.isMatch('abb', 'c*ab*')
assert s.isMatch('aa', '.*')
assert s.isMatch('ab', '.*')
assert s.isMatch('aadfga', 'a.*ga')
assert not s.isMatch('aewatg', 'a*watg')
assert s.isMatch('adasfe', 'a.aa*b*sfe')