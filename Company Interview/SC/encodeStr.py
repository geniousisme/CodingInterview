class Solution(object):
    def encode_str(self, string):
        char_freq_dict = {}
        for char in string:
            char_freq_dict[char] = char_freq_dict.get(char, 0) + 1

        result_str = ""
        for char in string:
            result_str += self.encode_char(char, char_freq_dict[char])

        return result_str

    def encode_char(self, char, freq):
        return '0' * (freq - 1) + '1'

if __name__ == "__main__":
	s = Solution()
	print s.encode_str("babccc")