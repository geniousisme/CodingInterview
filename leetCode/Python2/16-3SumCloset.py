class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # This question is very similar to 3Sum, but we just need to
        # calculate the closet sum in this nums
        nums.sort()
        min_diff = 9999
        res = 0
        length = len(nums)
        # since we will have two ptr after this one, just count until length - 2
        for i in xrange(length - 2):
            # left is the ptr ahead of this i
            # right is the ptr starting from the last index
            left = i + 1; right = length - 1
            # noew we sum the left & right, and there will be following cases
            while left < right:
                sum = nums[left] + nums[right] + nums[i]
                # if the sum is directly equal to target, just return
                if sum == target:
                    return sum
                # if not, then count the diff
                diff = abs(sum - target)
                # if the diff is smaller than min_diff, store it
                if diff < min_diff:
                    min_diff = diff
                    res = sum
                # now, try to move the ptr
                # if sum is bigger than target, we let right ptr move backward to reduce the sum
                if sum < target:
                    left += 1
                # if sum is smaller than target, we let left ptr move forward to increase the sum
                if sum > target:
                    right -= 1
        return res

if __name__ == "__main__":
    s = Solution()
    print s.threeSumClosest([-1, 2, 1, -4], 1)



