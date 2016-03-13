# Time:  O(m * n)
# Space: O(m + n)
#
# Given two numbers represented as strings, return multiplication of the numbers as a string.
# 
# Note: The numbers can be arbitrarily large and are non-negative.
#


class Solution1:
    # @param {string} num1
    # @param {string} num2
    # @return {string}
    def __init__(self):
        self.str_int_dict = \
        {                   \
          '0': 0,           \
          '1': 1,           \
          '2': 2,           \
          '3': 3,           \
          '4': 4,           \
          '5': 5,           \
          '6': 6,           \
          '7': 7,           \
          '8': 8,           \
          '9': 9            \
        }
    def builtInMultiply(self, num1, num2): # the fastest one
        return str(int(num1) * int(num2))

    def multiply(self, num1, num2):
        if len(num2) > len(num1): # length of num can decide which is bigger, ex. 12345 must be greater than 123
           return self.multiply(num2, num1)
        num1 = self.str2int(num1); num2 = self.str2int(num2)
        final_sum = 0
        while num2 > 0:
              tmp_sum = num1
              count   = 1
              while num2 >= count * 2:
                    count   = count * 2
                    tmp_sum = tmp_sum + tmp_sum
              num2      -= count
              final_sum +=  tmp_sum
        return str(final_sum)

    def str2int(self, string):
        digit        = len(string) - 1
        int_result   = 0
        for s in string:
            int_result += self.str_int_dict[s] * 10 ** digit
            digit      -= 1
        return int_result

class Solution(object):
    def multiply(self, num_str1, num_str2):
        num1_len = len(num_str1)
        num2_len = len(num_str2)
        num_str1 = num_str1[::-1]
        num_str2 = num_str2[::-1]
        arr = [0 for i in xrange(num1_len + num2_len)]
        for i in xrange(num1_len):
            for j in xrange(num2_len):
                arr[i + j] += int(num_str1[i]) * int(num_str2[j])
        carry = 0
        for i in xrange(num1_len + num2_len):
            arr[i] += carry
            carry  = arr[i] // 10
            arr[i] %= 10
        non_zero_idx = num1_len + num2_len - 1
        while arr[non_zero_idx] == 0:
            non_zero_idx -= 1
            if non_zero_idx == 0:
                break
        return "".join([str(arr[i]) for i in xrange(non_zero_idx, -1, -1)])
if __name__ == '__main__':
   s = Solution()
   print s.str2int('1345678900987654')
   print s.multiply('0', '9')

