class Solution(object):
    def threeSumJudge(self, nums):
        num_dict = {}
        for i in xrange(len(nums)):
            num_dict[nums[i]] = i
        for j in xrange(len(nums)):
            for i in xrange(j):
                sub_sum = -(nums[i] + nums[j])
                if sub_sum in num_dict and num_dict.get(sub_sum) != i and num_dict.get(sub_sum) != j:
                    return True
        return False

    def threeSum(self, nums):
        nums = sorted(nums)
        res = []
        length = len(nums)
        for i in xrange(len(nums) - 2):
            if i == 0 or nums[i] > nums[i - 1]: # notice this conditio!
                start = i + 1; end = len(nums) - 1
                while start < end:
                    if nums[start] + nums[end] == -nums[i]:
                        res.append([nums[i], nums[start], nums[end]])
                        start += 1; end -= 1
                        while start < end and nums[start] == nums[start - 1]:
                            start += 1
                        while start < end and nums[end] == nums[end + 1]:
                            end -= 1
                    elif nums[start] + nums[end] > -nums[i]:
                        end -= 1
                    else:
                        start += 1
        return res




if __name__ == "__main__":
    s = Solution()
    print s.threeSum([-2, 1, 0])
    print s.threeSum([0, 0, 0, 0])
