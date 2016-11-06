class Solution(object):
    def big_int_plus(self, num_str1, num_str2):
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
        while(i >= 0 or j >= 0):
            digit = self.char2int(num_str1, i) + self.char2int(num_str2, j)
            res_digit = (digit + carry) % 10
            carry = (digit + carry) // 10
            result = str(res_digit) + result
            i -= 1
            j -= 1
        if carry > 0:
            result = str(carry) + result
        return result

    def char2int(self, string, idx):
        return ord(string[idx]) - ord('0') if idx >= 0 else 0

if __name__ == "__main__":
    s = Solution()
    s.big_int_plus("100000000", "1")
    assert(s.big_int_plus("100000000", "1") == str(int("100000000") + int("1")))
    assert(s.big_int_plus("100000000", "0") == str(int("100000000") + int("0")))
    assert(s.big_int_plus("99999992222222", "11112233") == str(int("99999992222222") + int("11112233")))
    assert(s.big_int_plus("999999922222229999999", "11112233") == str(int("999999922222229999999") + int("11112233")))
    
