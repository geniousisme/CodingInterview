class Solution(object):
    def addDigitsJunior(self, num):
        """
        :type num: int
        :rtype: int
        """
        final_digit = num
        while final_digit > 9:
            final_digit = 0
            while num > 0:
                final_digit += num % 10
                num //= 10
            num = final_digit
        return final_digit

    def addDigits(self, num):
        if num == 0:
            return 0
        return num - 9 * ((num - 1) / 9)

if __name__ == "__main__":
    s = Solution()
    print s.addDigits(38)
    print s.addDigits(11)
    print s.addDigits(3)

