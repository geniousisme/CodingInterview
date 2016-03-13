# http://en.wikipedia.org/wiki/Quickselect
# find the kth smallest elements in O(n) time complexity & O(1) space
# sometimes it is better than heap to find the kth element

# you can see the leetcode questions:
# https://leetcode.com/problems/kth-largest-element-in-an-array/

import random
class Solution(object): # my own version, not done yet
    def findKthLargest(self, nums, k):
        if k < 1 or not nums:
            return 0
        # make the situation be able to suitable for quickselect(kth smallest)
        return self.get_kth(len(nums) - k + 1, nums, 0, len(nums) - 1)

    def get_kth_smallest(self, k, nums, start, end):
        print 'k', k
        pivot = nums[end]
        left = start; right = end - 1
        while left <= right:
            while nums[left] < pivot:
                left  += 1
            while nums[right] > pivot:
                right -= 1
            if left <= right:
                self.swap(nums, left, right)
                left  += 1
                right -= 1
        print "left"
        self.swap(nums, left, end)
        print "left", left
        print "right", right
        print nums
        if k == left + 1:
            return pivot
        elif k < left + 1:
            return self.get_kth_smallest(k, nums, start, right)
        else:
            return self.get_kth_smallest(k, nums, left, end)

    def swap(self, nums, idx1, idx2):
        nums[idx1], nums[idx2] = nums[idx2], nums[idx1]



if __name__ == "__main__":
    s = Solution()
    nums = [2, 6, 5, 1, 4, 9, 3]
    # print s.findKthLargest(nums, 1)
    # print s.findKthLargest(nums, 2)
    # print s.findKthLargest(nums, 3)
    # print s.findKthLargest(nums, 4)
    # print s.findKthLargest(nums, 5)
    # print s.findKthLargest(nums, 6)
    print s.get_kth_smallest(4, nums, 0, len(nums) - 1)
    print s.get_kth_smallest(5, nums, 0, len(nums) - 1)


