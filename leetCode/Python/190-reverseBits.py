# Time : O(logn) = O(32)
# Space: O(1)
#
# Reverse bits of a given 32 bits unsigned integer.
#
# For example, given input 43261596 (represented in binary as
# 00000010100101000001111010011100), return 964176192 (represented in binary
# as 00111001011110000010100101000000).
#
# Follow up:
# If this function is called many times, how would you optimize it?
#

class Solution1:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        bits = ''
        for i in xrange(31, -1, -1):
            number = 2 ** i
            if n < number:
               bits = '0' + bits 
               continue
            n -= number
            bits = '1' + bits
        return int(bits, 2)

class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        result = 0
        for i in xrange(32):
            result <<= 1
            result |= n & 1
            n >>= 1
        return result

if __name__ == '__main__':
  print Solution().reverseBits(1)
if __name__ == '__main__':
   s = Solution()
   print s.reverseBits(43261596)
