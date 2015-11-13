# Given a string s, partition s such that every substring of the partition is a palindrome.
#
# Return all possible palindrome partitioning of s.
#
# For example, given s = "aab",
# Return
#
#   [
#     ["aa","b"],
#     ["a","a","b"]
#   ]
class Solution:
    # @param s, a string
    # @return a list of lists of string
    '''
    TC: O(n^2 ~ 2^n)
    SC: O(n^2)
    dynamic programming solution
    '''
    def partition(self, s):
        n = len(s)

        is_palindrome = [[0 for j in xrange(n)] for i in xrange(n)]
        for i in reversed(xrange(0, n)):
            for j in xrange(i, n):
                is_palindrome[i][j] = s[i] == s[j] and ((j - i < 2 ) or is_palindrome[i + 1][j - 1])

        sub_partition = [[] for i in xrange(n)]
        for i in reversed(xrange(n)):
            for j in xrange(i, n):
                if is_palindrome[i][j]:
                    if j + 1 < n:
                        for p in sub_partition[j + 1]:
                            sub_partition[i].append([s[i:j + 1]] + p)
                    else:
                        sub_partition[i].append([s[i:j + 1]])

        return sub_partition[0]

class Solution(object):
    def __init__(self):
        self.res = []

    def partition(self, s):
        """
        TC: O(2 ^ n)
        SC: O(n ^ 2)
        """
        if self.res:
            self.res = []
        if s:
            self.partition_helper(s, [])
        return self.res

    def partition_helper(self, left_s, part):
        # basically, it is dfs
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
