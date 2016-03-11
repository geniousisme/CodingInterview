class Solution(object):
    def isOneEditDistance(self, str1, str2):
        if not str1 and not str2:
            return False

        if len(str1) > len(str2):
            return self.isOneEditDistance(str2, str1)

        len1 = len(str1); len2 = len(str2); i = 0; shifted = len2 - len1

        if shifted > 1:
            return False
        # super cool way to solve it! notice!
        while i < len1 and str1[i] == str2[i]:
            i += 1
        if shifted == 0: # if shifted biggern tham 0, just skip it
            i += 1
        while i < len1 and str1[i] == str2[i + shifted]:
            i += 1

        return i == len1

if __name__ == "__main__":
    s = Solution()
    print s.isOneEditDistance("aaaa", "aaa")
    print s.isOneEditDistance("aa", "a")
    print s.isOneEditDistance("ab", "acb")

