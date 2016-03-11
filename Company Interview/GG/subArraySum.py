def subArraySum(nums):
    dict = {0:-1}
    sum = 0
    res  = []
    for i in xrange(len(nums)):
        sum += nums[i]
        if dict.get(sum) is not None:
            res.append([dict.get(sum) + 1, i])
        else:
            dict[sum] = i
    return res