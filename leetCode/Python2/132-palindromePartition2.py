class Solution1(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        palindrome_table = self.init_palindrome_table(s)
        min_cuts = []

        for i in xrange(len(s) + 1):
            min_cuts.append(i - 1)

        for i in xrange(1, len(s) + 1):
            for j in xrange(i):
                if palindrome_table[j][i - 1]:
                    min_cuts[i] = min(min_cuts[j] + 1, min_cuts[i])

        return min_cuts[-1]

    def init_palindrome_table(self, s):
        palindrome_table = [[False for i in xrange(len(s))] for i in xrange(len(s))]

        for i in xrange(len(s)):
            palindrome_table[i][i] = True

        # for i in xrange(len(s) - 1):
        #     palindrome_table[i][i + 1] = s[i] == s[i + 1]

        for range in xrange(1, len(s)):
            start = 0
            while start + range < len(s):
                palindrome_table[start][start + range] = palindrome_table[start + 1][start + range - 1] and s[start] == s[start + range]
                start += 1
        return palindrome_table

class Solution:
    # @param s, a string
    # @return an integer
    def minCut(self, s):
        lookup = [[False for j in xrange(len(s))] for i in xrange(len(s))]
        mincut = [len(s) - 1 - i for i in xrange(len(s) + 1)]

        for i in xrange(len(s) - 1, -1, -1):
            for j in xrange(i, len(s)):
                if s[i] == s[j]  and (j - i < 2 or lookup[i + 1][j - 1]):
                    lookup[i][j] = True
                    mincut[i] = min(mincut[i], mincut[j + 1] + 1)
        print lookup
        print minxcut
        return mincut[0]

if __name__ == "__main__":
    s = Solution()
    print s.minCut("aab")