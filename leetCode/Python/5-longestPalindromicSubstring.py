# Given a string S, find the longest palindromic substring in S.
# You may assume that the maximum length of S is 1000, 
# and there exists one unique longest palindromic substring.

class Solution1:
    # @return a string
    def juniorLongestPalindrome(self, s):
        if len(s) <= 1: return s # for empty stirng and single char case
        longestPalin = ""
        for idx in xrange(len(s)):
            oddTmpPalin  = self.getLongestPalindrome(s, idx, idx)
            evenTmpPalin = self.getLongestPalindrome(s, idx, idx + 1)
            if len(oddTmpPalin)  > len(longestPalin):
               longestPalin = oddTmpPalin
            if len(evenTmpPalin) > len(longestPalin):
               longestPalin = evenTmpPalin
        return longestPalin

    def getLongestPalindrome(self, s, left, right):
        while left > -1 and right < len(s) and s[left] == s[right]:
              left  -= 1
              right += 1
        return s[left + 1 : right]

# Manacher's Algorithm
# http://leetcode.com/2011/11/longest-palindromic-substring-part-ii.html
class Solution:
    def longestPalindrome(self, s):
        '''
        TC: O(N)
        SC: O(N)
        '''
        string = self.preProcess(s)
        palindrome = [0] * len(string)
        center, right = 0, 0
        for i in xrange(1, len(string) - 1):
            i_mirror = 2 * center - i
            if right > i:
                palindrome[i] = min(right - i, palindrome[i_mirror])
            else:
                palindrome[i] = 0

            while string[i + 1 + palindrome[i]] == string[i - 1 - palindrome[i]]:
                palindrome[i] += 1

            if i + palindrome[i] > right:
                center, right = i, i + palindrome[i]

        max_len, max_center = 0, 0
        for i in xrange(1, len(string) - 1):
            if palindrome[i] > max_len:
                max_len = palindrome[i]
                max_center = i
        start = (max_center - 1 - max_len) / 2
        return s[start : start + max_len]

    def preProcess(self, s):
        if not s:
            return "^$"
        string = "^"
        for i in s:
            string +=  "#" + i
        string += "#$"
        return string
