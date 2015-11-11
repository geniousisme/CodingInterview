class Solution1:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        s_lst = s.strip().split(' ')
        print s_lst
        start = 0; end = len(s_lst)
        while start < end:
              if not s_lst[start]:
                 s_lst.pop(start)
                 end -= 1
                 continue
              start += 1
        print s_lst
        s_lst.reverse()
        return ' '.join(s_lst)

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s_list = s.split()
        return ' '.join(reversed(s_list))


if __name__ == '__main__':
   s = Solution()
   print s.reverseWords("the sky is blue")
   print s.reverseWords("    a    b   ")


