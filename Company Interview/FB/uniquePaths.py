class Solution1(object):
    '''
    Time:  O(m * n)
    Space: O(m * n)
    '''
    def unique_path_counts(self, m, n):
        dp = [[1 for i in xrange(n)] for j in xrange(m)]
        for i in xrange(1, m):
            for j in xrange(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[-1][-1]

class Solution2(object):
    '''
    Time:  O(m * n)
    Space: O(n)
    '''
    def unique_path_counts(self, m, n):
        if n > m:
            self.unique_path_counts(n, m)
        ways = [1] * n
        # each time use one n sized array to present the latest level of matrix
        for i in xrange(1, m):
            for j in xrange(1, n):
                ways[j] += ways[j - 1]
        return ways[-1]

from math import factorial
class Solution(object):
    '''
    Time:  O(m + n)
    Space: O(1)
    '''
    def unique_path_counts(self, m, n):
        if not m or not n:
            return 0
        return factorial(m + n - 2) / (factorial(n - 1) * factorial(m - 1))

if __name__ == '__main__':
   s = Solution()
   print s.unique_path_counts(3, 3)