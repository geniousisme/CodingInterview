class Solution(object):
    def lengthOfLongestSubstringI(self, s):
        """
        :type s: str
        :rtype: int
        some good reference:
        http://fisherlei.blogspot.com/2012/12/leetcode-longest-substring-without.html
        """
        start = 0; end = 1; longest_length = 1 if len(s) > 0 else 0
        position = {}
        while end < len(s):
            if s[end] in s[start:end]:
                # from the previous idx the char appear in the range [start, end] + 1
                start += s[start:end].find(s[end]) + 1
                end += 1
            else:
                end += 1
                longest_length = max(longest_length, end - start)
        return longest_length

    def lengthOfLongestSubstring(self, s): # with hash
        """
        :type s: str
        :rtype: int
        TC: O(N)
        SC: O(N)
        """
        longest_length = 0; last_repeated_pos = -1; positions = {}
        for i in xrange(len(s)):
            if s[i] in positions and positions[s[i]] > last_repeated_pos:
                last_repeated_pos = positions[s[i]]
            longest_length = max(longest_length, i - last_repeated_pos)
            positions[s[i]] = i
        return longest_length


if __name__ == "__main__":
    s = Solution()
    print s.lengthOfLongestSubstring("abcabcbb")
    print s.lengthOfLongestSubstring("abcbbbbeftgvdssbb")
    print s.lengthOfLongestSubstring("bbbb")
    print s.lengthOfLongestSubstring("b")
    print s.lengthOfLongestSubstring("adfewqbclo")
    print s.lengthOfLongestSubstring("aab")




