# Time:  O(n)
# Space: O(1)
#
# Given an integer array of size n, 
# find all elements that appear more than [n/3] times. 
# The algorithm should run in linear time and in O(1) space.
#

class Solution1:
    # @param {integer[]} nums
    # @return {integer[]}
    def majorityElement(self, nums):
        elem_dict = {}
        length    = len(nums)
        res       = []
        for i in xrange(length):
            elem_dict[nums[i]] = elem_dict.get(nums[i], 0) + 1
            if elem_dict[nums[i]] > length / 3:
               res.append(nums[i])
               elem_dict[nums[i]] = -length
        return res

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        candidate1 = candidate2 = None
        count1 = count2 = 0
        for n in nums:
            if candidate1 == n:
                count1 += 1
            elif candidate2 == n:
                count2 += 1
            elif count1 == 0:
                candidate1 = n
                count1 = 1
            elif count2 == 0:
                candidate2 = n
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1
        res = []
        count1 = count2 = 0
        for n in nums:
            if n == candidate1:
                count1 += 1
            elif n == candidate2:
                count2 += 1
        if count1 > len(nums) / 3:
            res.append(candidate1)
        if count2 > len(nums) / 3:
            res.append(candidate2)

        return res


if __name__ == '__main__':
   s = Solution()
   print s.majorityElement([1,1,1,1,1,1,1,2,4])
   print s.majorityElement([1,1,1,1,1,1])




        