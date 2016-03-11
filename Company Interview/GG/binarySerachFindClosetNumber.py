class Solution(object):
    def find_closet_number(self, nums, target):
        if not nums:
            return -1
        start = 0; end = len(nums) - 1; closest_candidate = 0; min_diff = float("inf")
        while start + 1 < end:
            mid = start + (end - start) / 2
            if nums[mid] == target:
                return target
            if abs(nums[mid] - target) < min_diff:
                min_diff = abs(nums[mid] - target)
                closest_candidate = nums[mid]
            if nums[mid] > target:
                end = mid
            else:
                start = mid
        if abs(target - nums[start]) < min_diff:
            return nums[start]
        if abs(target - nums[end]) < min_diff:
            return nums[end]
        return closest_candidate

if __name__ == "__main__":
    s = Solution()
    print s.find_closet_number([1, 2, 3, 3, 4, 5, 9, 10, 13], 0)
    print s.find_closet_number([1, 2, 3, 3, 4, 5, 9, 10, 13], 10)
    print s.find_closet_number([1, 2, 3, 3, 4, 5, 9, 10, 13], 11)
    print s.find_closet_number([1, 2, 3, 3, 4, 5, 9, 10, 13], 6)
    print s.find_closet_number([1, 2, 3, 3, 4, 5, 9, 10, 13], 7)



