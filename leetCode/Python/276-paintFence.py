# There is a fence with n posts, each post can be painted with one of the k colors.
# You have to paint all the posts such that no more than two adjacent fence posts have the same color.
# Return the total number of ways you can paint the fence.
# Note: n and k are non-negative integers.

# Time:  O(n)
# Space: O(1)

# DP solution with rolling window.
class Solution(object): # dp solution, just store the two latest results
    # s means same and stands for the last element of your dp1; d means different,
    # d1 and d2 stands for the last two elements of your dp2.
    # In each loop, dp1[i] = dp2[i - 1] turns into s = d2 and dp2[i] = (k - 1) * (dp2[i - 2] + dp2[i - 1])
    # becomes d2 = (k - 1) * (d1 + d2). Moreover, d1 needs to be set to the old d2,
    # which is recorded in s. So we have d1 = s.
    # Finally, the return value dp1[n - 1] + dp2[n - 1] is just s + d2.
    def numWays(self, n, k):
        """
        TC: O(n)
        SC: O(1)
        """
        if n < 2 or not k:
            return n * k
        same = k; diffs = k; next_diffs = k * (k - 1)
        for i in xrange(2, n):
            same = next_diffs
            next_diffs = (k - 1) * (diffs + next_diffs)
            diffs = same
        return same + next_diffs

class Solution2(object): # dp solution, use dp table to store the result
    def numWays(self, n, k):
        """
        TC: O(n)
        SC: O(n)
        """
        if n == 0:
            return 0
        elif n == 1:
            return k
        ways = [0] * n
        ways[0] = k
        ways[1] = (k - 1) * ways[0] + k
        for i in xrange(2, n):
            ways[i] = (k - 1) * (ways[i - 1] + ways[i - 2])
        return ways[n - 1]

if __name__ == "__main__":
     s2 = Solution2()
     print s2.numWays(3, 2)
     s = Solution()
     print s.numWays(3, 2)

