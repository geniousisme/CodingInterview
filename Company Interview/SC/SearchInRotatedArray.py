class Solution(object):
    def search(self, nums, target):
        if not nums:
            return -1
        start = 0
        end = len(nums) - 1

        while start + 1 < end:
            mid = (start + end) / 2
            if target == nums[mid]:
                return mid
            if nums[mid] >= nums[start]:
                if nums[start] <= target <= nums[mid]:
                    end = mid
                else:
                    start = mid
            else:
                if nums[mid] <= target <= nums[end]:
                    start = mid
                else:
                    end = mid
        if nums[start] == target:
            return start
        if nums[end] == target:
            return end
        return -1
