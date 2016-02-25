class ThreeSum(object):
    def threeSum(self, nums):
        nums = sorted(nums)
        res  = []
        length = len(nums)
        for i in xrange(length - 2):
            if i == 0 or nums[i] > nums[i - 1]:
                start = i + 1; end = length - 1
                while start < end:
                    if nums[start] + nums[end] == -nums[i]:
                        res.append([nums[i], nums[start], nums[end]])
                        start += 1
                        end   -= 1
                        while start < end and nums[end] == nums[end + 1]:
                            end -= 1
                        while start < end and nums[start] == nums[start - 1]:
                            start +=1
                    elif nums[start] + nums[end] > -nums[i]:
                        end -= 1
                    else:
                        start += 1
        return res
