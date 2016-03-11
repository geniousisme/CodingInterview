# A message containing letters from A-Z is
# being encoded to numbers using the following mapping:

# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26

# Given an encoded message containing digits, determine the total number of ways to decode it.

# For example,
# Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).

# The number of ways decoding "12" is 2.
class Solution(object): # if decode num is from 0 ~ 99
    def numDecodings(self, s):
        dp = [0 for _ in xrange(len(s) + 1)]
        dp[0] = 1
        for i in xrange(1, len(s) + 1):
            # if s[i - 1] != '0':
            dp[i] += dp[i - 1]
            if i > 1 and '1' <= s[i - 2] <= '9':
                dp[i] += dp[i - 2]
        return dp[len(s)]

class Solution(object): # if decode num is from 0 ~ 99
    def numDecodings(self, s):
        dp = [0 for _ in xrange(len(s) + 1)]
        dp[0] = 1
        for i in xrange(1, len(s) + 1):
            # if s[i - 1] != '0':
            dp[i] += dp[i - 1]
            if i > 1 and '1' <= s[i - 2] <= '9':
                dp[i] += dp[i - 2]
        return dp[len(s)]

class Solution0(object):
    def numDecodings(self, s):
        '''
        Time:  O(n)
        Space: O(1)
        '''
        if not s or s[0] == '0':
            return 0
        prev_prev, prev = 0, 1
        for i in xrange(len(s)):
            curr = 0
            if s[i] != '0':
                curr += prev
            if i > 0 and (s[i - 1] == '1' or (s[i - 1] == '2' and s[i] <= '6')):
                curr += prev_prev
            prev, prev_prev = curr, prev
        return prev

class Solution1(object):
    def numDecodings(self, s):
        '''
        Time:  O(n)
        Space: O(n)
        '''
        # if the s[0], which means there is no way to decode
        if not s or s[0] == '0':
            return 0
        dp = [0 for _ in xrange(len(s) + 1)]
        dp[0] = 1
        for i in xrange(1, len(s) + 1):
            # if there is not 0, 10, 20 case, then we can make sure that there is one way to decode
            if s[i - 1] != '0':
                dp[i] += dp[i - 1]
            # if the word is in the range of 10 ~ 26, which means they have one other way to decode, plus the before previous result
            if i > 1 and (s[i - 2] == '1' or (s[i - 2] == '2' and s[i - 1] <= '6')):
                dp[i] += dp[i - 2]
        return dp[len(s)]

class Solution2(object):
    '''
    Time:  O(n)
    Space: O(n)
    '''
    def numDecodings(self, s):
        if not s or s[0] == '0':
            return 0
        dp = [0 for _ in xrange(len(s) + 1)]
        dp[0] = 1
        dp[1] = 1 if s[0] != '0' else 0
        for i in xrange(1, len(s) + 1):
            if s[i - 1] != '0':
                dp[i] += dp[i - 1]
            if s[i - 2] == '1' or (s[i - 2] == '2' and s[i - 1] <= '6'):
                dp[i] += dp[i - 2]
        return dp[len(s)]

class Solution3(object):
    '''
    Time:  O(n)
    Space: O(1)
    '''
    def numDecodings(self, s):
        if not s or s[0] == '0':
            return 0
        current = 0
        prev_prev, prev = 0, 1
        for i in xrange(len(s)):
            current = 0
            if s[i] != '0':
                current = prev
            if i > 0 and (s[i - 1] == '1' or (s[i - 1] == '2' and s[i] <= '6')):
                current += prev_prev
            prev, prev_prev = current, prev
        return prev
if __name__ == "__main__":
    s = Solution()
    print s.numDecodings("919")
    print s.numDecodings("900")
    print s.numDecodings("0910")
    print s.numDecodings("100")
    print s.numDecodings("000")



