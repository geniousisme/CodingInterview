# Given an array nums, write a function to move all 0's
# to the end of it while maintaining the relative order of the non-zero elements.
# For example, given nums = [0, 1, 0, 3, 12],
# after calling your function, nums should be [1, 3, 12, 0, 0].

# Note:
# You must do this in-place without making a copy of the array.
# Minimize the total number of operations.

class Solution(object):
    '''
    Time:  O(n)
    Space: O(1)
    '''
    def moveZeroesWithOrder(self, nums):
        if not nums:
            return
        non_zero_idx = idx = 0
        while idx < len(nums):
            if nums[idx] != 0:
                nums[non_zero_idx], nums[idx] = nums[idx], nums[non_zero_idx]
                non_zero_idx += 1
            idx += 1

    def moveZeroesWithOrder(self, nums):
        non_zero_idx = 0
        for i in xrange(len(nums)):
            if nums[i] != 0:
                nums[non_zero_idx] = nums[i]
                non_zero_idx += 1
        for i in xrange(non_zero_idx, len(nums)):
            nums[i] = 0

class Solution2(object):
    '''
    Time:  O(n)
    Space: O(1)
    '''
    def moveZeroesWithoutOrder(self, nums):
        # dont need to maintain the original order, minize the swap times
        # the minimize swap times will be equal to the number of zero numbers
        if not nums:
            return
        zero_idx = len(nums) - 1; idx = 0
        while idx < zero_idx:
            if nums[idx] == 0:
                nums[zero_idx], nums[idx] = nums[idx], nums[zero_idx]
                zero_idx -= 1
            else:
                idx += 1


if __name__ == "__main__":
    s2 = Solution2()
    nums = [0, 1, 0, 3, 12]
    s2.moveZeroesWithoutOrder(nums)
    print nums
    nums = [0, 0, 0]
    s2.moveZeroesWithoutOrder(nums)
    print nums
    nums = [0, 0, 1]
    s2.moveZeroesWithoutOrder(nums)
    print nums