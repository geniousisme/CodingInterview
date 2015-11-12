class Solution:
    # @param {string} s
    # @param {string} t
    # @return {boolean}
    def isIsomorphicI(self, s, t):
        length = len(s)
        dictionary = {}
        if length == 1:
           return s == t
        for i in xrange(length):
            replace = dictionary.get(s[i])
            if replace:
               if replace != t[i]:
                  return False
            else:
               if t[i] in dictionary.values():
                  return False
               dictionary[s[i]] = t[i]
        return True

    def isIsomorphic(self, str1, str2):
        if len(str1) != len(str2):
            return False
        return self.is_isomorphic_check(str1, str2) and self.is_isomorphic_check(str2, str1)

    def is_isomorphic_check(self, str1, str2):
        dict = {}
        for i in xrange(len(str1)):
            if dict.get(str1[i]) is None:
                dict[str1[i]] = str2[i]
            else:
                if dict.get(str1[i]) != str2[i]:
                    return False
        return True



if __name__ == '__main__':
   s = Solution()
   print s.isIsomorphic('egg', 'add')
   print s.isIsomorphic('foo', 'bar')
   print s.isIsomorphic('bar', 'foo')
   print s.isIsomorphic('title', 'paper')
   print s.isIsomorphic('ab', 'aa')