class Solution1:
    # @param s, a string
    # @return a list of lists of string
    def __init__(self):
        self.res = []
    
    def partition(self, s):
        if s:
           self.recursivePart(s, [])
        return self.res

    def recursivePart(self, left_s, part):
        if not left_s:
           self.res.append(part)
           return
        for i in xrange(1, len(left_s) + 1):
            if self.checkPalindrome(left_s[:i]):
               self.recursivePart(left_s[i:], part + [left_s[:i]])
    
    def checkPalindrome(self, s):
        start = 0; end = len(s) - 1
        while start < end:
              if s[start] != s[end]:
                 return False
              start += 1; end -= 1
        return True

class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        res = []
        self.partition_helper(s, res, [])
        return res

    def partition_helper(self, left_s, res, part):
        if not left_s:
            res.append(list(part))
            return
        for i in xrange(1, len(left_s) + 1):
            if self.is_palindrome(left_s[:i]):
                part.append(left_s[:i])
                self.partition_helper(left_s[i:], res, part)
                part.pop()

    def is_palindrome(self, s):
        end = len(s) - 1; start = 0
        while end > start:
            if s[end] != s[start]:
                return False
            end   -= 1
            start += 1
        return True

if __name__ == '__main__':
   s = Solution()
   print s.partition('aab')