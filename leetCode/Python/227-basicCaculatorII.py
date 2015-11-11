# Time:  O(n)
# Space: O(n)
#
# Implement a basic calculator to evaluate a simple expression string.
#
# The expression string contains only non-negative integers, +, -, *, / 
# operators and empty spaces . The integer division should truncate toward zero.
#
# You may assume that the given expression is always valid.
#
# Some examples:
# "3+2*2" = 7
# " 3/2 " = 1
# " 3+5 / 2 " = 5
# Note: Do not use the eval built-in library function.
#


class Solution:
    # @param {string} s
    # @return {integer}
    # Chris::TODO: take this as reference:
    # http://www.wengweitao.com/leetcode-basic-calculator.html
    def calculate(self, s):
        length = len(s)
        if length == 0: 
           return 0
        ans = last_num = op = i = 0
        num = ''
        sign = 1
        # op = 0: +, -
        # op = 1: *
        # op = 2: /
        while i < length:
            if s[i] == ' ':
               i += 1
               continue
            
            if '9' >= s[i] >= '0':
                num = ''
                while i < length and '9' >= s[i] >= '0':
                      num += s[i]
                      i += 1
                i -= 1
                if op == 1:
                   last_num *= int(num)
                elif op == 2:
                     last_num /= int(num)
                else: # op == 0, +, -
                     last_num = int(num)

            if s[i] == '+':
               ans += sign * last_num
               op   = 0 
               sign = 1

            elif s[i] == '-':
                 ans += sign * last_num
                 op   = 0
                 sign = -1
            
            elif s[i] == '*':
                 op   = 1
                 
            elif s[i] == '/':
                 op   = 2
            
            i += 1
        
        ans += sign * last_num

        return ans

class Solution:
    # @param {string} s
    # @return {integer}
    def calculate(self, s):
        operands, operators = [], []
        operand = ""
        for i in reversed(xrange(len(s))):
            if s[i].isdigit():
                operand += s[i]
                if i == 0  or not s[i-1].isdigit():
                    operands.append(int(operand[::-1]))
                    operand = ""
            elif s[i] == ')' or s[i] == '*' or s[i] == '/':
                operators.append(s[i])
            elif s[i] == '+' or s[i] == '-':
                while operators and \
                      (operators[-1] == '*' or operators[-1] == '/'):
                    self.compute(operands, operators)
                operators.append(s[i])
            elif s[i] == '(':
                while operators[-1] != ')':
                    self.compute(operands, operators)
                operators.pop()

        while operators:
            self.compute(operands, operators)

        return operands[-1]

    def compute(self, operands, operators):
        left, right = operands.pop(), operands.pop()
        op = operators.pop()
        if op == '+':
            operands.append(left + right)
        elif op == '-':
            operands.append(left - right)
        elif op == '*':
            operands.append(left * right)
        elif op == '/':
            operands.append(left / right)

if __name__ == '__main__':
   s = Solution()
   # print s.calculate("3+2*2")
   # print s.calculate(" 3/2 ")
   # print s.calculate(" 3+5 / 2 ")
   print s.calculate("2*3+4")

   