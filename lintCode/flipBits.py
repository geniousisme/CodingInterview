class Solution:
    """
    @param a, b: Two integer
    return: An integer
    """
    def bitSwapRequired(self, a, b):
        # write your code here
        xor_bit = a ^ b
        count = 0
        for _ in xrange(32):
            if xor_bit & 1:
                count += 1
            xor_bit >>= 1
        return count

if __name__ == "__main__":
    s = Solution()
    print s.bitSwapRequired(31, 14)