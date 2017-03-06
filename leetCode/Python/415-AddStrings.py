class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if not (num1 or num2):
            return "0"

        if not num1:
            return num2

        if not num2:
            return num1

        i1 = len(num1) - 1
        i2 = len(num2) - 1

        digit = carry = 0
        res = ""

        while i1 >= 0 or i2 >= 0:
            digit = carry

            if i1 >= 0:
                digit += int(num1[i1])
                i1 -= 1

            if i2 >= 0:
                digit += int(num2[i2])
                i2 -= 1

            carry = digit // 10
            res = str(digit % 10) + res

        if carry > 0:
            res = str(carry) + res

        return res

if __name__ == "__main__":
    s = Solution()
    print s.addStrings("123", "456")
    print s.addStrings("9133", "0")
    print s.addStrings("99", "9")






