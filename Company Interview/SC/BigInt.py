class Solution(object):
    def big_int_add(self, num_str1, num_str2):
        if not num_str1:
            return num_str2

        if not num_str2:
            return num_str1

        num1_len = len(num_str1)
        num2_len = len(num_str2)
        result_len = max(num1_len, num2_len) + 1
        result = ""

        i = num1_len - 1
        j = num2_len - 1
        carry = 0
        while i >= 0 or j >= 0:
            digit = self.char2int(num_str1, i) + self.char2int(num_str2, j)
            res_digit = (digit + carry) % 10
            carry = (digit + carry) // 10
            result = str(res_digit) + result
            i -= 1
            j -= 1
        if carry > 0:
            result = str(carry) + result
        return result

    def big_int_substract(self, num_str1, num_str2):
        if not num_str1:
            return num_str2

        if not num_str2:
            return num_str1

        num1_len = len(num_str1)
        num2_len = len(num_str2)
        if num2_len > num1_len:
           return self.big_int_substract(num_str2, num_str1)
        
        i = num1_len - 1
        j = num2_len - 1
        carry = 0

        result = []
        while i >= 0 or j >= 0:
            res_digit = self.char2int(num_str1, i) + carry - self.char2int(num_str2, j)
            if res_digit < 0:
                res_digit += 10
                carry = -1
            else:
                carry = 0
            result.insert(0, str(res_digit))
            i -= 1
            j -= 1

        # remove trailing zero in the front
        while result[0] == '0':
            result.pop(0)

        return ''.join(result)

    def char2int(self, string, idx):
        return ord(string[idx]) - ord('0') if idx >= 0 else 0

if __name__ == "__main__":
    s = Solution()
    assert(s.big_int_add("100000000", "1") == str(int("100000000") + int("1")))
    assert(s.big_int_add("100000000", "0") == str(int("100000000") + int("0")))
    assert(s.big_int_add("99999992222222", "11112233") == str(int("99999992222222") + int("11112233")))
    assert(s.big_int_add("999999922222229999999", "11112233") == str(int("999999922222229999999") + int("11112233")))
    assert(s.big_int_add("999999922222229999999", "999999999999999999999999911112233") == str(int("999999922222229999999") + int("999999999999999999999999911112233")))

    assert(s.big_int_substract("100000000", "1") == str(int("100000000") - int("1")))
    assert(s.big_int_substract("100000000", "0") == str(int("100000000") - int("0")))
    assert(s.big_int_substract("99999992222222", "11112233") == str(int("99999992222222") - int("11112233")))
    assert(s.big_int_substract("999999922222229999999", "11112233") == str(int("999999922222229999999") - int("11112233")))
    assert(s.big_int_substract("999999922222229999999", "999999999999999999999999911112233") == str(int("999999999999999999999999911112233") - int("999999922222229999999")))
    assert(s.big_int_substract("1000000", "999999") == str(int("1000000") - int("999999")))
    assert(s.big_int_substract("10", "10") == str(int("10") - int("10")))


    
