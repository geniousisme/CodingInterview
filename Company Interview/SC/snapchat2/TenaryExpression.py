class Solution(object):
    def parseTernary(self, expression):
        """
        :type expression: str
        :rtype: str
        """
        if not expression:
            return ""
        stack = []
        for ch in reversed(expression):
            if stack and stack[-1] == '?':

                stack.pop()
                first, second = '', ''
                while stack and stack[-1] != ':':
                    first += stack.pop()

                stack.pop()
                while stack and stack[-1] != ':':
                    second += stack.pop()

                # first, _, second = stack.pop(), stack.pop(), stack.pop()
                stack.append(first if ch == 'T' else second)
            else:
                stack.append(ch)
        return stack[0]



s = Solution()
assert s.parseTernary("T?23:3") == '23'
assert s.parseTernary("F?1:T?4:5") == '4'
assert s.parseTernary("T?T?F:5:3") == 'F'
