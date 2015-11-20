# Time:  O(n * 2^n)
# Space: O(2^n)
#
# The count-and-say sequence is the sequence of integers beginning as follows:
# 1, 11, 21, 1211, 111221, ...
#
# 1 is read off as "one 1" or 11.
# 11 is read off as "two 1s" or 21.
# 21 is read off as "one 2, then one 1" or 1211.
# Given an integer n, generate the nth sequence.
#
# Note: The sequence of integers will be represented as a string.
#

class Solution:
    # @return a string
    def countAndSay(self, n):
        def countStr(n, string):
            if not n:
               return string
            count = 1; prev  = string[0]; result = ""; str_len = len(string)
            for i in xrange(1, str_len + 1):
                if i == str_len:
                   result = "".join([result, str(count), prev])
                   break
                if prev != string[i]:
                   result = "".join([result, str(count), prev])
                   count = 0
                count += 1
                prev = string[i]
            return countStr(n - 1, result)

        if n >= 1:
           return countStr(n - 1, "1")
        else:
           return ""

if __name__ == '__main__':
   s = Solution()
   print s.countAndSay(0)




