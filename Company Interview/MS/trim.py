


class Solution(object):
	def trim(self, input_str):
		char_list = list(input_str)
		start = 0; end = len(char_list) - 1
		while char_list[start] == ' ' or char_list[end] == ' ':
			if char_list[start] == ' ':
				start += 1
			if char_list[end] == ' ':
				end -= 1
		char_list = char_list[start:end + 1]
		start = 0
		while start < len(char_list):
			if char_list[start] != ' ':
				start += 1
			else:
				start_nxt = start + 1
				while char_list[start_nxt] == ' ':
					char_list.pop(start_nxt)
				start = start_nxt
		print char_list
		return ''.join(char_list)

if __name__ == "__main__":
	s = Solution()
	test_str = '   a    bbb b cc c     c d       ddd d dd     d       e'
	print s.trim(test_str)
	print s.trim(test_str) == te


