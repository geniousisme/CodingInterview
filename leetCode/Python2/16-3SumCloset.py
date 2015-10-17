class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        min_diff = 9999
        res = 0
        length = len(nums)
        for i in xrange(length - 2):
            left = i + 1; right = length - 1
            while left < right:
                sum = nums[left] + nums[right] + nums[i]
                if sum == target:
                    return sum
                diff = abs(sum - target)
                if diff < min_diff:
                    min_diff = diff
                    res = sum
                if sum < target:
                    left += 1
                if sum > target:
                    right -= 1
        return res

if __name__ == "__main__":
    s = Solution()
    print s.threeSumClosest([-1, 2, 1, -4], 1)



