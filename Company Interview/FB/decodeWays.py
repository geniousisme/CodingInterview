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
class Solution1(object):
    '''
    Time:  O(n)
    Space: O(n)
    '''
    def numDecodings(self, s):
        if not s or s[0] == '0':
            return 0
        dp = [0] * (len(s) + 1)
        dp[0] = 1; dp[1] = 1 if s[0] != '0' else 0
        for i in xrange(2, len(s) + 1):
            if s[i - 1] != '0':
                dp[i] += dp[i - 1]
            if s[i - 2] == '1' or (s[i - 2] == '2' and s[i - 1] <= '6'):
                dp[i] += dp[i - 2]
        return dp[len(s)]

class Solution2(object):
    '''
    Time:  O(n)
    Space: O(1)
    '''
    def numDecodings(self, s):
        if not s or s[0] == '0':
            return 0
        prev_prev = 1
        prev = 1 if s[0] != '0' else 0
        for i in xrange(2, len(s) + 1):
            curr = 0
            if s[i - 1] != '0':
                curr = prev
            if s[i - 2] == '1' or (s[i - 2] == '2' and s[i - 1] <= '6'):
                curr += prev_prev
            prev, prev_prev = curr, prev
        return prev

class Solution(object):
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
    s = Solution1()
    print s.numDecodings("2")