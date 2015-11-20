# Numbers can be regarded as product of its factors. For example,

# 8 = 2 x 2 x 2;
#   = 2 x 4.
# Write a function that takes an integer n and
# return all possible combinations of its factors.

# Note:
# Each combination's factors must be sorted ascending,
# for example: The factors of 2 and 6 is [2, 6], not [6, 2].
# You may assume that n is always positive.
# Factors should be greater than 1 and less than n.
# Examples:
# 1. input: 1,  output: []
# 2. input: 37, output: []
# 3. input: 12,
# output:
# [
#   [2, 6],
#   [2, 2, 3],
#   [3, 4]
# ]
# 4. input: 32
# output:
# [
#   [2, 16],
#   [2, 2, 8],
#   [2, 2, 2, 4],
#   [2, 2, 2, 2, 2],
#   [2, 4, 4],
#   [4, 8]
# ]

class Solution:
    # @param {integer} n
    # @return {integer[][]}
    '''
    Time:  O(nlogn)
    Space: O(logn)
    '''
    def getFactors(self, n):
        res = []
        factors = []
        self.get_factor_combs(n, res, factors)
        return res

    def get_factor_combs(self, n, res, factors):
        factor = 2 if not factors else factors[-1]
        while factor ** 2 <= n:
            if n % factor == 0:
                factors.append(factor)
                factors.append(n / factor)
                res.append(list(factors))
                factors.pop()
                self.get_factor_combs(n / factor, res, factors)
                factors.pop()
            factor += 1

if __name__ == "__main__":
    s = Solution()
    print s.getFactors(32)


