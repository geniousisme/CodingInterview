import random

def shuffle(nums):
    for i in xrange(len(nums)):
        replace = int(random.random() * (len(nums) - i) + i)
        nums[replace], nums[i] = nums[i], nums[replace]

if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    shuffle(nums)
    print nums