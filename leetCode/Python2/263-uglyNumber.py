class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num < 1:
            return False
        for i in [2, 3, 5]:
            while num % i == 0:
                num /= i
        return num == 1

if __name__ == "__main__":
     s = Solution()
     print s.isUgly(30)
     print s.isUgly(10)
     print s.isUgly(14)

