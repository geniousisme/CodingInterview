# Implement regular expression matching with support for '.' and '*'.
#
# '.' Matches any single character.
# '*' Matches zero or more of the preceding element.
#
# The matching should cover the entire input string (not partial).
#
# The function prototype should be:
# bool isMatch(const char *s, const char *p)
#
# Some examples:
# isMatch("aa","a") -> false
# isMatch("aa","aa") -> true
# isMatch("aaa","aa") -> false
# isMatch("aa", "a*") -> true
# isMatch("aa", ".*") -> true
# isMatch("ab", ".*") -> true
# isMatch("aab", "c*a*b") -> true
#


class DPSolution(object): # dp solution
    def isMatch(self, s, p):
        '''
        TC: O(m * n)
        SC: O(m * n)
        '''
        # Initialization
        dp = [[False for j in xrange(len(p) + 1)] for i in xrange(len(s) + 1)]

        dp[0][0] = True

        for j in xrange(1, len(p) + 1):
            if j >= 2 and p[j - 1] == '*':
                # need to check the previous previous result
                dp[0][j] = dp[0][j - 2]

        for i in xrange(1, len(s) + 1):
            for j in xrange(1, len(p) + 1):
                # if it is . case
                if p[j - 1] == '.':
                    # then we just use the previous result
                    dp[i][j] = dp[i - 1][j - 1]
                # if it is * case, more complex!
                elif p[j - 1] == '*':
                    # need to check the previous or before previous result for pattern,
                    # or check previous string match to previous previous pattern or not.
                    # if previous pattern matches current string, or previous pattern is ., then match to anything
                    # the reason why I need to check dp[i][j - 2] is that * can match zero number of current string,
                    # which means it can skip this one if it doesn't match.
                    dp[i][j] = dp[i][j - 1] or dp[i][j - 2] or (dp[i - 1][j] and (s[i - 1] == p[j - 2] or p[j - 2] == '.'))
                else:
                    # last case is the common case, match current pattern and string & previous result.
                    dp[i][j] = dp[i - 1][j - 1] and s[i - 1] == p[j - 1]
        return dp[-1][-1]

class Solution(object): # recursive
    # @return a boolean
    def isMatch(self, s, p):
        # if no p, then the s should also be ""
        if not p:
            return not s
        # first, check if p[1] == '*' or not
        if len(p) == 1 or p[1] != '*':
            # check if the first elems of s & p are equal or first elem of p is '.'
            if len(s) > 0 and (p[0] == s[0] or p[0] == '.'):
                return self.isMatch(s[1:], p[1:])
            else:
                return False
        else:
            # len(p) > 1 and p[1] == '*'
            while len(s) > 0 and (p[0] == s[0] or p[0] == '.'):
                if self.isMatch(s, p[2:]): # p[1] == '*' case
                    return True
                # match, move s forward
                s = s[1:]
            # not match, move forward to check
            return self.isMatch(s, p[2:])


if __name__ == '__main__':
   s = Solution()
   string = 'cab'
   pattern = 'c*a*b'
   print s.isMatch(string, pattern)
   string = '..*'
   pattern = 'cab'
   print s.isMatch(string, pattern)