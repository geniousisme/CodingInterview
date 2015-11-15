class Solution1(object):
    def rotate(self, nums, k):
        '''
        TC: O(n)
        SC: O(n)
        '''
        k %= len(nums)
        rotate_len = len(nums) - k
        nums.extend(nums[:rotate_len])
        del nums[:rotate_len]

class Solution(object):
    def rotate(self, nums, k):
        """
        TC: O(n)
        SC: O(1)
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        self.reverse(nums, 0, len(nums) - 1)
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, len(nums) - 1)

    def reverse(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            end   -= 1
            start += 1