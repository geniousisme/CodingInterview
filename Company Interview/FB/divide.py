class Solution(object):
    '''
    Time:  O(logn)
    Space: O(1)
    notice the negative & over flow condition!
    '''
    def divide(self, dividend, divisor):
        INF = 2147483647
        if dividend == 0:
            return 0
        if divisor == 0:
            return INF
        dvd, dvs, quotient = abs(dividend), abs(divisor), 0 # notice for the negative number
        while dvd >= dvs:
            count = 1
            dvs_sum = dvs
            while dvd > dvs_sum * 2:
                dvs_sum *= 2
                count += count
            dvd -= dvs_sum
            quotient += count
        # notice the overflow condition
        if quotient >= INF:
            quotient = INF
        if (dividend < 0 and divisor > 0) or (dividend < 0 and divisor > 0):
            if quotient < INF:
                return -quotient
            else:
                return -quotient - 1
        return quotient