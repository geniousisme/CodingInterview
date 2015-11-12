# Time:  O(n^2)
# Space: O(n)
#
# Given a string s and a dictionary of words dict,
# determine if s can be segmented into a space-separated sequence of one or more dictionary words.
#
# For example, given
# s = "leetcode",
# dict = ["leet", "code"].
#
# Return true because "leetcode" can be segmented as "leet code".
#

class Solution:
    # @param s, a string
    # @param wordDict, a set<string>
    # @return a boolean
    # Chris:TODO: figure out how to know that they want to use DP
    def wordBreak(self, s, wordDict):
        dp = [True]
        for i in xrange(1, len(s) + 1):
            dp.append(False)
            for j in xrange(i):
                if dp[j] and s[j:i] in wordDict:
                   dp[i] = True
        # print dp
        return dp[-1]

if __name__ == '__main__':
   s = Solution()
   print s.wordBreak('leetcode', ['leet', 'code'])