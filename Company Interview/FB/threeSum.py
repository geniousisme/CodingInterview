class Solution(object):
    def threeSum(self, nums):
        num_dict = {}
        for i in xrange(len(nums)):
            num_dict[nums[i]] = i
        for j in xrange(len(nums)):
            for i in xrange(j):
                sub_sum = -(nums[i] + nums[j])
                if sub_sum in num_dict and num_dict.get(sub_sum) != i and num_dict.get(sub_sum) != j:
                    return True
        return False


if __name__ == "__main__":
    s = Solution()
    print s.threeSum([-2, 1, 0])
    print s.threeSum([0, 0, 0, 0])
