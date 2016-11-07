class Solution(object):
    def mySqrt(self, x):
        start = 1
        end = x
        while start + 1 < end:
            mid = (start + end) / 2
            if mid ** 2 == x:
                return mid
            elif mid ** 2 > x:
                end = mid
            else:
                start = mid
        if x >= end * end:
            return end
        return start