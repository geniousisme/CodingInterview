class Solution:
    """
    @param nums: The integer array you should partition
    @param k: As description
    @return: The index after partition
    """
    def partitionArray(self, nums, k):
        # write your code here
        # you should partition the nums by k
        # and return the partition index as description
        pivot = k
        left = 0; right = len(nums) - 1
        while left <= right: # notice the edge condition
            while left <= right and nums[left] < pivot:
                left += 1
            while left <= right and nums[right] >= pivot:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        return left

if __name__ == "__main__":
    s = Solution()
    print s.partitionArray([3, 2, 2, 1], 2)
    print s.partitionArray([3, 2, 2, 1], 4)
    print s.partitionArray([3, 2, 2, 1], 3)


