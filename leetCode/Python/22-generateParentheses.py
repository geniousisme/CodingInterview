# Time:  O(4^n / n^(3/2)) ~= Catalan numbers
# Space: O(n)
#
# Given n pairs of parentheses, write a function to generate
# all combinations of well-formed parentheses.
#
# For example, given n = 3, a solution set is:
#
# "((()))", "(()())", "(())()", "()(())", "()()()"
#

class Solution1:
    # @param an integer
    # @return a list of string
    def dfs_parenth(self, left, right, string, result):
        if right < left:
           return
        if right == 0 and left == 0:
           result.append(string)
        if right > 0:
           self.dfs_parenth(left, right - 1, string + ')', result)
        if left  > 0:
           self.dfs_parenth(left - 1, right, string + '(', result)

    def generateParenthesis(self, n):
        result = []
        if n > 0:
           self.dfs_parenth(n, n, '', result)
        return result

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

if __name__ == '__main__':
   s = Solution()
   print s.generateParenthesis(3)