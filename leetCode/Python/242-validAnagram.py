class Solution1:
    # @param {string} s
    # @param {string} t
    # @return {boolean}
    def isAnagram(self, s, t):
        '''
        Time:  O(nlogn)
        Space: O(1)
        '''
        slst = list(s)
        tlst = list(t)
        slst = sorted(slst)
        tlst = sorted(tlst)
        return slst == tlst

class Solution:
    def isAnagram(self, s, t):
        '''
        Time:  O(n)
        Space: O(n)
        '''
        if len(s) != len(t):
            return False
        sdict = {}; tdict = {}
        for str in s:
            sdict[str] = sdict.get(str, 0) + 1
        for str in t:
            tdict[str] = tdict.get(str, 0) + 1
        for s in sdict:
            if sdict[s] != tdict.get(s):
                return False
        return True