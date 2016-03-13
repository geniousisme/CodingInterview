class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        final_sum = 10
        while final_sum >= 10:
            final_sum = 0
            while n >= 10:
               unit = n % 10
               n //= 10
               final_sum += unit * unit
            final_sum += n * n
            n = final_sum
        return final_sum == 1

if __name__ == "__main__":
    s = Solution()
    print s.isHappy(19)
    print s.isHappy(32)
    print s.isHappy(14)
