class Solution:
    #@param n, m: Two integer
    #@param i, j: Two bit positions
    #return: An integer
    def updateBits(self, n, m, i, j):
        # write your code here
        for _ in xrange(i):
            n >>= 1
        n |= m
        for _ in xrange(i):
            n <<= 1
        return n
