class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        for i in xrange(32):
            count += (n & 0x01)
            n >>= 1
        return count

if __name__ == "__main__":
    s = Solution()
    print s.hammingWeight(11)
    print s.hammingWeight(3)
    print s.hammingWeight(4)
    print s.hammingWeight(0)


