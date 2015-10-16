class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        length = len(s)
        if length > 0:
            if length % 2 == 1: # can avoid some unsymmetric situation
                return False
            stack.append(s[0]) # notice: be careful for null input!
            for i in xrange(1, length):
                if s[i] == ']':
                    if stack[-1] != '[':
                        return False
                    else:
                        stack.pop()
                elif s[i] == '}':
                    if stack[-1] != '{':
                        return False
                    else:
                        stack.pop()
                elif s[i] == ')':
                    if stack[-1] != '(':
                        return False
                    else:
                        stack.pop()
                else:
                    stack.append(s[i])
        return stack == []

    def isValid(self, s):
