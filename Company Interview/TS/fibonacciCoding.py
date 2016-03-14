class Solution(object):
    def __init__(self):
        self.dp = [1, 1]

    def encode(self, num):
        if len(self.dp) != 2:
            self.dp = [1, 1]
        start = 2
        while self.dp[-1] <= num:
            self.dp.append(self.dp[start - 1] + self.dp[start - 2])
            start += 1
            if self.dp[-1] > num:
                self.dp.pop()
                break
        code_words = ''
        for fib_idx in xrange(len(self.dp) - 1, -1, -1):
            if self.dp[fib_idx] > num:
                code_words += '0'
            else:
                num -= self.dp[fib_idx]
                code_words += '1'
        return code_words

if __name__ == "__main__":
    s = Solution()
    for num in xrange(1, 31):
        print num, s.encode(num)


