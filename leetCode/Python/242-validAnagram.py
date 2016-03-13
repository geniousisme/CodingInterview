# Given two strings s and t, write a function 
# to determine if t is an anagram of s.

# For example,
# s = "anagram", t = "nagaram", return true.
# s = "rat", t = "car", return false.

# Note:
# You may assume the string contains only lowercase alphabets.


class Solution(object):
    def isAnagram(self, s, t):
        '''
        Time:  O(nlogn)
        Space: O(1)
        '''
        return sorted(s) == sorted(t)

class Solution(object):
    def isAnagram(self, s, t):
        '''
        Time:  O(n)
        Space: O(n)
        '''
        if len(s) != len(t):
            return False
        tdict = {}; sdict = {}
        for char in s:
            sdict[char] = sdict.get(char, 0) + 1
        for char in t:
            tdict[char] = tdict.get(char, 0) + 1
        for char in s:
            if sdict.get(char) != tdict.get(char):
                return False
        return True

