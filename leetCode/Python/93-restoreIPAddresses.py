# Time:  O(n^m) = O(3^4)
# Space: O(n * m) = O(3 * 4)
#
# Given a string containing only digits, restore it by returning all possible valid IP address combinations.
#
# For example:
# Given "25525511135",
#
# return ["255.255.11.135", "255.255.111.35"]. (Order does not matter)
#


class Solution:
    # @param {string} s
    # @return {string[]}
    # for more detail, read this website for this algo:
    # http://www.cnblogs.com/zuoyuan/p/3768112.html

    def __init__(self):
        self.res = []
    
    def restoreIpAddresses(self, s):
        self.DFS(s, 0, "")
        return self.res
        
    def DFS(self, s, part, ip):
        if part == 4: # there are four parts in this array
           if not s:  # s == ''
              self.res.append(ip[1:])
           return
        for i in xrange(1, 4):
            if i <= len(s): # i > len(s) make error!
               # print 's:', s
               sub = s[:i]
               if int(sub) <= 255: # accept only zero in the mid and hv only len 1
                  self.DFS(s[i:], part + 1, ip + '.' + sub)
               if s[0] == '0': return # keep '00' out of array
            else:
               return 

if __name__ == '__main__':
   s = Solution()
   print s.restoreIpAddresses("25525511135")
   s = Solution()
   print s.restoreIpAddresses("0000")

