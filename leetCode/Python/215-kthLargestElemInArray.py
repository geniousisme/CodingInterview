import random

class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {integer}
    def findKthLargest(self, nums, k):
        '''
        Time:  O(n)
        Space: O(n)
        '''
        pivot = random.choice(nums)
        nums1 = []; nums2 = []
        length = len(nums)
        for i in xrange(length):
            if nums[i] > pivot:
                nums1.append(nums[i])
            elif nums[i] < pivot:
                 nums2.append(nums[i])
        if k <= len(nums1):
           return self.findKthLargest(nums1, k)
        elif k > length - len(nums2):
             return self.findKthLargest(nums2, k - (length - len(nums2)))
        else:
             return pivot

class Solution2(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        pivot = nums[0]
        tail = 0
        for i in range(1, len(nums)):
            if nums[i] > pivot:
                tail += 1
                nums[tail], nums[i] = nums[i], nums[tail]

        nums[tail], nums[0] = nums[0], nums[tail]
        if tail + 1 == k:
            return pivot
        elif tail + 1 < k:
            return self.findKthLargest(nums[tail+1:], k - tail - 1)
        else:
            return self.findKthLargest(nums[:tail], k)  #excluding pivot

if __name__ == '__main__':
   s = Solution()
   test = [2,4,5,6,1,0,3,10]
   print sorted(test)
   print s.findKthLargest(test, 1)



        