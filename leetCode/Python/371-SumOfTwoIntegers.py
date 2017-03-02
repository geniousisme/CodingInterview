class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        Take reference:
        https://www.hrwhisper.me/leetcode-sum-two-integers/
        http://bookshadow.com/weblog/2016/06/30/leetcode-sum-of-two-integers/
        https://zh.wikipedia.org/wiki/%E4%BA%8C%E8%A3%9C%E6%95%B8

        """
        MAX_INT = 0x7FFFFFFF
        MAX_UPPER = 0xFFFFFFFF

        while b:
            a, b = (a ^ b) % MAX_UPPER, ((a & b) << 1) % MAX_UPPER

        return a if a <= MAX_INT else ~(a & MAX_INT) ^ MAX_INT
