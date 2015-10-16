class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        length = len(s)
        if length > 0:
            if length % 2 == 1: # can avoid some unsmetric situation
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
        return not stack

    def isValidGoogle(self, str): # google version
        stack = []
        for s in str:
            if s == '(':
                stack.append(s)
            elif s == ')':
                if stack:
                    stack.pop()
                else:
                    return False
        return not stack

if __name__ == "__main__":
    s = Solution()
    print s.isValidGoogle("(google)rocks")
    print s.isValidGoogle("(goo)(gle)()rocks")
    print s.isValidGoogle("goo((gle))rocks")
    print s.isValidGoogle("google((rocks)")
    print s.isValidGoogle("google((rocks))))")




