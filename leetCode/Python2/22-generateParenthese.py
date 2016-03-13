class Solution(object):
    def __init__(self):
        self.res = []
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.res = []
        self.parenthese_helper(n, n, "")
        return self.res

    def parenthese_helper(self, left, right, parenthese):
        if left > right:
            return
        if left == 0 and right == 0:
            self.res.append(parenthese)
            return
        if left > 0:
            self.parenthese_helper(left - 1, right, parenthese + '(')
        if right > 0:
            self.parenthese_helper(left, right - 1, parenthese + ')')

# good reference: https://zh.wikipedia.org/wiki/%E5%8D%A1%E5%A1%94%E5%85%B0%E6%95%B0

if __name__ == "__main__":
    s = Solution()
    print s.generateParenthesis(2)
    print s.generateParenthesis(3)