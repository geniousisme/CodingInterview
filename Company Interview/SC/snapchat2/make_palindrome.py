def make_palindrome(s):
    """
    give a string s, you can add, remove, or change one char at any
    position. what the minimum steps to change the string to palindrome?
    """
    length = len(s)
    dp = [[0]*length for _ in xrange(length)]

    for l in xrange(2,  length+1):
        for i in xrange(length-l+1):
            j = i + l -1
            if s[i] == s[j]:
                dp[i][j] = dp[i+1][j-1]
            else:
                dp[i][j] = min(dp[i+1][j], dp[i+1][j-1], dp[i][j-1]) + 1
    return dp[0][-1]

print make_palindrome('adcba')
print make_palindrome('adcda')
print make_palindrome('abcde')
print make_palindrome('asdfsa')

