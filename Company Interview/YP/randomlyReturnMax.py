import random

class Solution(object):
    def randomMaxIdx(self, nums):
        maximum = -float("inf")
        max_idx = 0
        max_num = 0
        for i in xrange(len(nums)):
            if nums[i] > maximum:
                maximum = nums[i]
                max_idx = i
                max_num = 1
            if nums[i] == maximum:
                max_num += 1
                if random.random() < 1 / max_num:
                    max_idx = i
        return max_idx

if __name__ == "__main__":
    s = Solution()
    print s.randomMaxIdx([-1, 3, 2, 3, 3])
    print s.randomMaxIdx([2, 4, 6, 6, 3, 1, 6, 6])
