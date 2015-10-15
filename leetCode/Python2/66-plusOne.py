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
        pass