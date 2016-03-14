class Solution(object): # in-place swap solution
    def partition(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        negative_ptr = 0
        for i in xrange(len(nums)):
            if nums[i] < 0:
                nums.insert(negative_ptr, nums.pop(i))
                negative_ptr += 1
            
if __name__ == "__main__":
    s = Solution()
    test1 = [2 ,3 ,4, -1, -2, 5, -4, 0, -3]
    s.partition(test1)
    print test1
        