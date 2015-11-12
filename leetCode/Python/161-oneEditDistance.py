class Solution:
    # @param {string} s
    # @param {string} t
    # @return {boolean}
    def isOneEditDistance(self, s, t):
        if not s and not t:
           return False
        slen = len(s); tlen = len(t)
        if tlen >= slen:
           return self.oneEditDistanceJudge(s, t, slen, tlen)
        else:
           return self.oneEditDistanceJudge(t, s, tlen, slen)

    def oneEditDistanceJudge(self, s, t, slen, tlen):
        # edit distance more than 1, return False
        if tlen - slen > 1:
           return False
        # len is equal, then check difference between words
        # if difference more than one, return False
        # if difference more is one,
        elif tlen == slen:
             count = 0
             for i in xrange(tlen):
                 if s[i] != t[i]:
                    count += 1
             return count == 1
        else: # tlen - slen == 1
        # just more than one,
        # then check the following string is equal or not.
             for i in xrange(slen):
                 if s[i] != t[i]:
                    return s[i:] == t[i + 1:]
             return True

if __name__ == '__main__':
   s = Solution()
   print s.isOneEditDistance("a", "")
   print s.isOneEditDistance("aab", "ab")
   print s.isOneEditDistance("aac", "aab")
   print s.isOneEditDistance("ac", "ab")
   print s.isOneEditDistance("ab", "ab")





