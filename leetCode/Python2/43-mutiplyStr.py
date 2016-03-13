class Solution(object):
    def multiply(self, num_str1, num_str2):
        num1_len = len(num_str1)
        num2_len = len(num_str2)
        # reverse string first, multiply from low unit to high unit
        num_str1 = num_str1[::-1]
        num_str2 = num_str2[::-1]
        arr = [0 for i in xrange(num1_len + num2_len)]
        # let each unit multiply with others, save it into an array to deal with carry
        for i in xrange(num1_len):
            for j in xrange(num2_len):
                arr[i + j] += int(num_str1[i]) * int(num_str2[j])
        carry = 0
        # deal with carry
        for i in xrange(num1_len + num2_len):
            arr[i] += carry
            carry  = arr[i] // 10
            arr[i] %= 10
        # clean up the trailing zero
        non_zero_idx = num1_len + num2_len - 1
        while arr[non_zero_idx] == 0:
            non_zero_idx -= 1
            if non_zero_idx == 0: # notice the whole zero case
                break
        # finally, combine all int in array together and return as str
        return "".join([str(arr[i]) for i in xrange(non_zero_idx, -1, -1)])

if __name__ == "__main__":
    s = Solution()
    print s.multiply("123", "456")
    print s.multiply("2", "12")
    print s.multiply("0", "0")




