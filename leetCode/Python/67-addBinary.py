# Given two binary strings, return their sum (also a binary string).
# For example,
# a = "11"
# b = "1"
# Return "100".

class Solution1(object):
    def addBinary(self, a, b):
        """
        Time:  O(n)
        Space: O(n)
        """
        a = a[::-1]
        b = b[::-1]
        ai = bi = carry = 0; res = []
        while ai < len(a) and bi < len(b):
            curr = int(a[ai]) + int(b[bi]) + carry
            carry = curr // 2
            res.append(str(curr % 2))
            ai += 1; bi += 1
        while ai < len(a):
            curr = int(a[ai]) + carry
            carry = curr // 2
            res.append(str(curr % 2))
            ai += 1
        while bi < len(b):
            curr = int(b[bi]) + carry
            carry = curr // 2
            res.append(str(curr % 2))
            bi += 1
        if carry:
            res.append(str(carry))
        return ''.join(reversed(res))

class Solution(object):
    def addBinary(self, a, b):
        '''
        Time:  O(n)
        Space: O(n)
        '''
        ai = len(a) - 1; bi = len(b) - 1; curr = carry = 0; res = ""
        while ai >= 0 or bi >= 0:
            if ai >= 0:
                curr += int(a[ai])
                ai -= 1
            if bi >= 0:
                curr += int(b[bi])
                bi -= 1
            curr += carry
            carry = curr // 2
            res += str(curr % 2)
        if carry:
            res += str(carry)
        return res[::-1]

if __name__ == '__main__':
   s = Solution()
   a = '111'
   b = '1'
   print s.addBinary(a, b)