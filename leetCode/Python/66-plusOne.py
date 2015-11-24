# Given a non-negative number represented as an array of digits, plus one to the number.

# The digits are stored such that the most significant digit is at the head of the list.



class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        Time:  O(n)
        Space: O(1)
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