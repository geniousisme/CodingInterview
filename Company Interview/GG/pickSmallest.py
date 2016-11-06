class Solution(object):
	def pickSmallest(self, num):
		current_largest_num = float("inf")
		for i in xrange(len(num) - 1):
			replace_int = num[i] if num[i] > num[i + 1] else num[i + 1]
			temp = int(num[:i] + replace_int + num[i + 2:])
			if temp < current_largest_num:
				current_largest_num = temp
		return current_largest_num

if __name__ == "__main__":
	s = Solution()
	print s.pickSmallest("233614")
	print s.pickSmallest("1578")
	print s.pickSmallest("135")
	print s.pickSmallest("10000")
