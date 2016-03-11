import collections

class Solution(object):
    def fourSum(self, nums):
        num_dict = collections.defaultdict(list)
        for i in xrange(len(nums)):
            for j in xrange(i + 1, len(nums)):
                num_dict[nums[i] + nums[j]].append((i, j))

        for i in xrange(len(nums)):
            for j in xrange(i + 1, len(nums) - 2): # since we will add two extra idx for 
                if target - (nums[i] + nums[j]) in num_dict:
                    for idx_tuple in num_dict[target - (nums[i] + nums[j])]:
                        if idx_tuple[0] > j:
                            return True
        return False

