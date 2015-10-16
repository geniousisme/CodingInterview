class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        length = len(digits)
        carry  = 1
        for i in xrange(length - 1, -1, -1):
            next_num  = digits[i] + carry
            digits[i] = next_num % 10
            carry     = next_num // 10
        if carry > 0:
            digits.insert(0, 1)
        return digits

    def minusOne(self, digits):
        digits[0] *= -1
        neg_carry = -1
        length = len(digits)
        for i in xrange(length - 1, -1, -1):
            if digits[i] + neg_carry < 0:
                digits[i] = 9
                neg_carry = -1
            else:
                digits[i] += neg_carry
                neg_carry = 0
        if digits[0] == 0:
            del digits[0]
        digits[0] *= -1
        return digits

if __name__ == "__main__":
    s = Solution()
    print s.minusOne([-1, 0, 0, 0])
    print s.minusOne([-1, 9, 2, 8])
