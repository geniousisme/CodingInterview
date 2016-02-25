class Solution:
    # @param x, an integer
    # @return an integer
    def mySqrt(self, x):
        if x == 0:
            return 0
        start = 1; end = x / 2 + 1
        while( start + 1 < end ):
            center = ( start + end ) / 2
            if center ** 2 == x:
                return center
            elif center ** 2 > x:
                start = center
            else:
                end = center
        return start