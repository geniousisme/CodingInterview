import operator


def calculator(s):
    """
    With only +-*/
    """
    s = s.replace(' ', '')
    ops = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.div}
    priority = {'+': 1, '-': 1, '*': 2, '/': 2, '$': 0}
    stack = []
    num = 0

    for ch in s+'$':
        if ch.isdigit():
            num = num * 10 + int(ch)
        else:
            # operator met
            stack.append(num)
            num = 0
            while len(stack) > 2 and priority[stack[-2]] >= priority[ch]:
                right, op, left = stack.pop(), stack.pop(), stack.pop()
                stack.append(ops[op](left, right))
            stack.append(ch)
    return stack[0]


def calculator2(s):
    """
    With only +-*/ and ()
    """
    s = s.replace(' ', '')
    ops = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.div}
    priority = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 0, ')': 0, '$': -1}
    stack = []
    num = ''

    for ch in s+'$':
        if ch.isdigit():
            num = num + ch
        else:
            if num:
                stack.append(int(num))
                num = ''
            if ch == '(':
                stack.append(ch)
            elif ch == '-' and (not stack or stack[-1] in ops.keys() or stack[-1] == '('):
                num = '-'
            else:
                while len(stack) > 1 and priority[stack[-2]] >= priority[ch]:
                    right, op = stack.pop(), stack.pop()
                    if op == '(':
                        stack.append(right)
                        break
                    left = stack.pop()
                    stack.append(ops[op](left, right))
                if ch != ')':
                    stack.append(ch)
    return stack[0]


def test(s):
    assert calculator2(s) == eval(s)

test('-5-1+(3*7-9)/(-3)+90*23/(-34*98-3)')