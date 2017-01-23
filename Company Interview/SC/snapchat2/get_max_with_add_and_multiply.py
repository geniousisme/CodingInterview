def my_get_max(nums):
    length = len(nums)
    dp = [[0]*length for _ in xrange(length)]

    for i in xrange(length):
        dp[i][i] = nums[i]

    for l in xrange(2, length+1):
        for i in xrange(length-l+1):
            j = i + l - 1
            for k in xrange(i, j):
                dp[i][j] = max(dp[i][k] + dp[k+1][j], dp[i][k] * dp[k+1][j], dp[i][j])
    return dp[0][-1]

print my_get_max([1,2,3])