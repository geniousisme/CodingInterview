class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        Time:  O(mn), m is the longest string length
        Space: O(1)
        """
        if not strs:
            return ""
        longest_prefix = strs[0]
        for i in xrange(1, len(strs)):
            idx = 0
            while idx < len(longest_prefix) and idx < len(strs[i]) and longest_prefix[idx] == strs[i][idx]:
                idx += 1
            longest_prefix = longest_prefix[:idx]
        return longest_prefix
