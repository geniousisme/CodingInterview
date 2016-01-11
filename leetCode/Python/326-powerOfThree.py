import math

class Solution1(object): # use log to calculate
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n < 1:
            return False
        return n == 3 ** round((math.log(n, 3)))

class Solution(object): # iterative
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n < 1:
            return False
        while n > 1:
            if n % 3 != 0:
                return False
            n /= 3
        return True

class Solution(object): # recursive
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        if n == 1:
            return True
        return n % 3 == 0 and self.isPowerOfThree(n // 3)