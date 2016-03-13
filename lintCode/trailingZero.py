class Solution:
    # @param n a integer
    # @return ans a integer
    def trailingZeros(self, n):
        zero_num = 0
        while n > 5:
            n = n // 5
            zero_num += n
        return zero_num

if __name__ == "__main__":
    s = Solution()
    print s.trailingZeros(11)
    print s.trailingZeros(105)



