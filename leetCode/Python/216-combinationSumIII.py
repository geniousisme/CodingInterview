# Time:  O(k * C(n, k))
# Space: O(k)
#
# Find all possible combinations of k numbers that add up to a number n,
# given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.
#
# Ensure that numbers within the set are sorted in ascending order.
#
#
# Example 1:
#
# Input: k = 3, n = 7
#
# Output:
#
# [[1,2,4]]
#
# Example 2:
#
# Input: k = 3, n = 9
#
# Output:
#
# [[1,2,6], [1,3,5], [2,3,4]]
#


class Solution:
    # @param {integer} k
    # @param {integer} n
    # @return {integer[][]}
    def combinationSum3(self, k, n):
        if k > 0:
           res = []; comb = []
           self.recCombination(0, k, 0, n, comb, res)
        return res

    def recCombination(self, curr, k, count, left, comb, res):
        if left == 0 and count == k:
           res.append(comb)
           return
        for i in xrange(curr + 1, 10):
            self.recCombination(i, k, count + 1, left - i, comb + [i], res)


if __name__ == '__main__':
   s = Solution()
   print s.combinationSum3(3, 7)
   print s.combinationSum3(3, 9)
