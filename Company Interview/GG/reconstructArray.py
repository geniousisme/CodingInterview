'''
A= [2, 4, 1, 3, 5]
B = [0, 0, 2, 1, 0]
[1, 2, 3, 4, 5]
[1, 2, 3, 4]
[1,2,4]
[2, 4]
[2]
'''
def reconstruct(nums):
    if not nums:
         return []
    original_nums = range(1, n + 1) # 1 - 5
    res = [0] * len(nums)
    for i in xrange(len(nums) - 1, -1, -1):
         res[i] = original_nums[len(original_nums) - nums[i] -1]
         del original_nums[len(original_nums) - nums[i] -1]
    return res
