# Given a 2D binary matrix filled with 0's and 1's
# find the largest square containing all 1's and return its area.
#
# For example, given the following matrix:
#
# 1 0 1 0 0
# 1 0 1 1 1
# 1 1 1 1 1
# 1 0 0 1 0
# Return 4.
#

class Solution(object):
    # @param {character[][]} matrix
    # @return {integer}
    def maximalSquare(self, matrix):
        if not matrix:
            return 0
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * n for x in xrange(m)]
        ans = 0
        for x in xrange(m):
            for y in xrange(n):
                dp[x][y] = int(matrix[x][y])
                if x and y and dp[x][y]:
                    dp[x][y] = min(dp[x - 1][y - 1], dp[x][y - 1], dp[x - 1][y]) + 1
                ans = max(ans, dp[x][y])
        return ans * ans

if __name__ == '__main__':
   s = Solution()
   test = [                           \
            ['1', '0', '1', '0', '0'],\
            ['1', '0', '1', '1', '1'],\
            ['1', '1', '1', '1', '1'],\
            ['1', '0', '1', '1', '1'] \
          ]
   print s.maximalSquare(test)
   # print test

   test2 = [['1', '0', '1']]
   print s.maximalSquare(test2)

   test3 = ['1']
   print s.maximalSquare(test3)
