# A message containing letters from A-Z is being encoded
# to numbers using the following mapping:
#
# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
# Given an encoded message containing digits,
# determine the total number of ways to decode it.
#
# For example,
# Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).
#
# The number of ways decoding "12" is 2.
#

class Solution1(object):
    def numDecodings(self, s):
        '''
        TC: O(N)
        SC: O(N)
        '''
        if not s or s[0] == '0':
            return 0
        dp = [1, 1]
        for i in xrange(2, len(s) + 1):
            sub = s[i - 2:i]
            if 10 <= int(sub) <= 26:
                if sub[1] != '0':
                    dp.append(dp[i - 1] + dp[i - 2])
                else:  # "10" or "20"
                    dp.append(dp[i - 2])
            elif s[i - 1] != '0':
                dp.append(dp[i - 1])
            else:
                return 0
        return dp[len(s)]

class Solution2(object):
    def numDecodings(self, s):
        '''
        TC: O(N)
        SC: O(1)
        '''
        if not s or s[0] == '0':
            return 0
        prev_prev = 0
        prev      = 1
        for i in xrange(len(s)):
            curr = 0
            if s[i] != '0':
                curr = prev
            if i > 0 and (s[i - 1] == '1' or (s[i - 1] == '2' and s[i] <= '6')):
                curr += prev_prev
            prev, prev_prev = curr, prev
        return prev




if __name__ == "__main__":
    s = Solution2()
    print s.numDecodings("123")
    # print s.numDecodings("210")
    # print s.numDecodings("240")


