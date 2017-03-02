class Solution1(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = []
        for i in xrange(len(s) - 1, -1, -1):
            res.append(s[i])
        return "".join(res)

class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s[::-1]

if __name__ == "__main__":
    s = Solution()
    print s.reverseString("Hello")
