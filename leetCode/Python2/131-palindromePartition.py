class Solution(object):
    def __init__(self):
        self.res = []

    def partition(self, s):
        """
        TC: O(n ^ 2 ~ 2 ^ n)
        SC: O(n ^ 2)
        """
        if self.res:
            self.res = []
        if s:
            self.partition_helper(s, [])
        return self.res

    def partition_helper(self, left_s, part):
        if not left_s:
            self.res.append(part)
            return
        for i in xrange(1, len(left_s) + 1): # notice the edge case! (1 ~ len(s) +1)
            if self.is_palindrome(left_s[:i]):
                self.partition_helper(left_s[i:], part + [left_s[:i]])

    def is_palindrome(self, string):
        for i in xrange(len(string) // 2):
            if string[i] != string[len(string) - i - 1]:
                return False
        return True

if __name__ == "__main__":
    s = Solution()
    print s.partition("aab")

