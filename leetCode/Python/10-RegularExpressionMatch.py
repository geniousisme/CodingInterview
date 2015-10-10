#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    # @return a boolean
    def isMatch(self, s, p):
        dp=[[False for i in range(len(p)+1)] for j in range(len(s)+1)]
        dp[0][0]=True
        # self.printDP(s, p, dp)
        for i in range(1,len(p)+1):
            if p[i-1]=='*':
                if i>=2:
                    dp[0][i]=dp[0][i-2]
        # self.printDP(s, p, dp)
        for i in range(1,len(s)+1):
            for j in range(1,len(p)+1):
                if p[j-1]=='.':
                    dp[i][j]=dp[i-1][j-1]
                elif p[j-1]=='*':
                    dp[i][j]=dp[i][j-1] or dp[i][j-2] or (dp[i-1][j] and (s[i-1]==p[j-2] or p[j-2]=='.'))
                else:
                    dp[i][j]=dp[i-1][j-1] and s[i-1]==p[j-1]
                # self.printDP(s, p, dp)

        return dp[len(s)][len(p)]

    def printDP(self, s, p, dp):
        for i in range(len(s)+1):
            line_data = ""
            for j in range(len(p)+1):
                if dp[i][j]:
                    line_data += "T "
                else:
                    line_data += "F "
            print line_data


if __name__ == '__main__':
   s = Solution()
   string = 'cab'
   pattern = 'c*a*b'
   print s.isMatch(string, pattern)
   string = '..*'
   pattern = 'cab'
   print s.isMatch(string, pattern)