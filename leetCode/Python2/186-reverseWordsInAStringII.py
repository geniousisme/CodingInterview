class Solution(object):
    def reverseWords(self, s):
        """
        :type s: a list of 1 length strings (List[str])
        :rtype: nothing
        """
        start = end = 0
        while end < len(s):
            if s[end] != ' ':
                end += 1
            else:
                self.reverse(s, start, end - 1)
                start = end = end + 1
        self.reverse(s, start, end - 1)
        self.reverse(s, 0, end - 1)

    def reverse(self, str_list, start, end):
        while start < end:
            str_list[start], str_list[end] = str_list[end], str_list[start]
            start += 1
            end   -= 1

if __name__ == "__main__":
    s = Solution()
    print s.reverseWords(['t', 'h', 'e', ' ', 's', 'k', 'y', ' ', 'i', 's', ' ', 'b', 'l', 'u', 'e'])