class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        idx_dict = {}
        for i in xrange(len(nums)):
            if idx_dict.get(target - nums[i]) is not None:
                return [idx_dict[target - nums[i]] + 1, i + 1]
            idx_dict[nums[i]] = i

if __name__ == "__main__":
    s = Solution()
    print s.twoSum([2, 7, 11, 15], 13)
