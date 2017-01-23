def play(nums):
    if len(nums) == 1:
        return nums[0]
    return sum(nums) - min(play(nums[1:]), play(nums[:-1]))


# def play2(nums):
#     length = len(nums)
#     dp = [[0]*length for _ in xrange(length)]
#
#     for i in xrange(length):
#         dp[i][i] = nums[i]
#
#     for l in xrange(2, length+1):
#         for i in xrange(length-l+1):
#             j = i + l -1
#             dp[i][j] = sum(nums[i:j+1]) - min(dp[i][j-1], dp[i+1][j])
#     return dp[0][-1]


def play2(nums):
    length = len(nums)

    dp = [[0]*length for _ in xrange(length)]
    pre_sum = [[0] * (length+1)]

    for i in xrange(length):
        pre_sum[i+1] = pre_sum[i] + nums[i]

    for i in xrange(length):
        dp[i][i] = nums[i]

    for l in xrange(2, length+1):
        for i in xrange(length-l+1):
            j = i + l -1
            dp[i][j] = pre_sum[j+1] - pre_sum[i] - min(dp[i + 1][j], dp[i - 1][j])

    return dp[0][-1]


a = [4,56,2,3,4,3,34,6,4,35,6]


def test(a):
    assert play(a) == play2(a)
