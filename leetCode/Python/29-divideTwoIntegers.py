# Divide two integers without using multiplication, division and mod operator.
# If it is overflow, return MAX_INT.

class Solution1:
    def divide(self, dividend, divisor):
        quotient = divisor_sum = 0; flag = 1
        if (dividend < 0) ^ (divisor < 0): # XOR dividend < 0, divisor < 0
            flag = -1
        dividend = abs(dividend); divisor = abs(divisor)
        while dividend >= divisor:      # divide two level of this algorithm,
              count = 1                 # first, if dividend is still bigger than                                        # than divisor but smaller than divisor_sum
              divisor_sum = divisor
              while divisor_sum * 2 <= dividend:
                    divisor_sum += divisor_sum
                    count       += count
              dividend -= divisor_sum
              quotient += count
        result = quotient * flag
        if result > 2 ** 31 - 1:
           return 2 ** 31 - 1
        if result < -2 ** 31:
           return -2 ** 31
        return result

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

if __name__ == "__main__":
   s = Solution()
   print s.divide(2 ** 32, 1)