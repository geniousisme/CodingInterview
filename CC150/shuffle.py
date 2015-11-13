import random

def shuffle(self, nums):
    for i in xrange(len(nums)):
        replace = random.random() * (len(nums) - i) + i
        swap(nums, i, replace)

def swap(nums, idx1, idx2):
    tmp = nums[idx1]
    nums[idx1] = nums[idx2]
    nums[idx2] = tmp