class BigInt(object):
    def multiply(self, num_str1, num_str2):
        if not (num_str1 or num_str2):
            return 0
        
        if not num_str1:
            return num_str2

        if not num_str2:
            return num_str1

        num1_len = len(num_str1)
        num2_len = len(num_str2)
        res_len = num1_len + num2_len
        result = [0] * res_len

        num_str1 = num_str1[::-1]
        num_str2 = num_str2[::-1]

        for i in xrange(num1_len):
            for j in xrange(num2_len):
                result[i + j] += int(num_str1[i]) * int(num_str2[j])

        carry = 0
        for i in xrange(res_len):
            digit = result[i] + carry
            result[i] = digit % 10
            carry = digit // 10

        while result[-1] == 0 and len(result) > 1:
            result.pop()

        return ''.join([str(result[i]) for i in xrange(len(result) - 1, -1, -1)])


    def add(self, num_str1, num_str2):
        if not (num_str1 or num_str2):
            return 0
        
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
            result = self.int2char(res_digit) + result
            i -= 1
            j -= 1
        if carry > 0:
            result = self.int2char(carry) + result
        return result

    def substract(self, num_str1, num_str2, is_negative=False):
        if not (num_str1 or num_str2):
            return 0
        
        if not num_str1:
            return num_str2

        if not num_str2:
            return num_str1

        num1_len = len(num_str1)
        num2_len = len(num_str2)
        if num2_len > num1_len:
           return self.substract(num_str2, num_str1, True)
        if num2_len == num1_len:
            i = num1_len - 1
            while i >= 0 and num_str2[i] == num_str1[i]:
                i -= 1
            if num_str2[i] > num_str1[i]:
                return self.substract(num_str2, num_str1, True)
        
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
            result.insert(0, self.int2char(res_digit))
            i -= 1
            j -= 1

        # remove trailing zero in the front
        while len(result) > 1 and result[0] == '0':
            result.pop(0)

        return ['', '-'][is_negative] + ''.join(result)


    def char2int(self, string, idx):
        return ord(string[idx]) - ord('0') if idx >= 0 else 0

    def int2char(self, integer):
        return chr(integer + 48)

if __name__ == "__main__":
    big_int = BigInt()
    assert(big_int.add("100000000", "1") == str(int("100000000") + int("1")))
    assert(big_int.add("100000000", "0") == str(int("100000000") + int("0")))
    assert(big_int.add("99999992222222", "11112233") == str(int("99999992222222") + int("11112233")))
    assert(big_int.add("999999922222229999999", "11112233") == str(int("999999922222229999999") + int("11112233")))
    assert(big_int.add("999999922222229999999", "999999999999999999999999911112233") == str(int("999999922222229999999") + int("999999999999999999999999911112233")))

    assert(big_int.substract("100000000", "1") == str(int("100000000") - int("1")))
    assert(big_int.substract("100000000", "0") == str(int("100000000") - int("0")))
    assert(big_int.substract("99999992222222", "11112233") == str(int("99999992222222") - int("11112233")))
    assert(big_int.substract("999999922222229999999", "11112233") == str(int("999999922222229999999") - int("11112233")))
    assert(big_int.substract("999999922222229999999", "999999999999999999999999911112233") == str(int("999999922222229999999") - int("999999999999999999999999911112233")))
    assert(big_int.substract("1000000", "999999") == str(int("1000000") - int("999999")))
    assert(big_int.substract("10", "10") == str(int("10") - int("10")))
    assert(big_int.substract("999", "100000") == str(int("999") - int("100000")))
    assert(big_int.substract("111", "999") == str(int("111") - int("999")))
