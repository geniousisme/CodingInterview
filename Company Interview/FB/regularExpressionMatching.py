class Solution(object):
    def isMatch(self, string, pattern):
        if not pattern:
            return not string
        if len(pattern) == 1 or pattern[1] != "*":
                if len(string) > 0 and (pattern[0] == string[0] or pattern[0] == '.'):
                    return self.isMatch(string[1:], pattern[1:])
        else:
            while len(string) > 0 and (pattern[0] == string[0] or pattern[0] == '.'):
                if self.isMatch(string, pattern[2:]):
                    return True
                string = string[1:]
            return self.isMatch(string, pattern[2:])

class Solution(object):
    def isMatch(self, string, pattern):
        dp = [[False for _ in xrange(len(pattern) + 1)] for _ in xrange(len(string) + 1)]
        dp[0][0] = True
        for j in xrange(2, len(pattern) + 1):
            if pattern[j - 1] == "*":
                dp[0][j] = dp[0][j - 2]
        for i in xrange(1, len(string) + 1):
            for j in xrange(1, len(pattern) + 1):
                if pattern[j - 1] == ".":
                    dp[i][j] = dp[i - 1][j - 1]
                elif pattern[j - 1] == "*":
                    dp[i][j] = dp[i][j - 1] or dp[i][j - 2] or (dp[i - 1][j] and (string[i - 1] == pattern[j - 2] or pattern[j - 2] == '.'))
                else:
                    dp[i][j] = dp[i - 1][j - 1] and string[i - 1] == pattern[j - 1]
        return dp[-1][-1]
