'''
Given an array of non-negative integers, 
you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

For example:
A = [2,3,1,1,4], return true.

A = [3,2,1,0,4], return false.
'''
class Solution:
    # @param {integer[]} nums
    # @return {boolean}
    def canJump(self, nums):
        '''
        Time:  O(n)
        Space: O(1)
        '''
        length   = len(nums)
        curr_idx = length - 1
        i        = length - 2
        # go to iterate the index from last(curr_idx) & second last index(i) of the list
        # if i + nums[i] >= curr_idx, which means I ca reach this curr_idx from this idx
        # then change curr_idx to i, and keep track the previous idx(i - 1)
        # the reason why we need to keep it is that it might have some situation that
        # the idx can reach the destination at first time, so you need to keep track it.
        while i > -1:
              if i + nums[i] >= curr_idx:
                 curr_idx = i
              i -= 1
        # if the final curr_idx is not 0, which means 0 index cannot reach the destination
        # it it can, then it can jump to
        if not curr_idx:
           return True
        return False

if __name__ == '__main__':
   s = Solution()
   print s.canJump([2,3,1,1,4])
   print s.canJump([2, 2, 2, 1, 4])
   print s.canJump([1, 1, 1, 1, 2, 0, 0])
   print s.canJump([3, 2, 1, 0, 4])
   print s.canJump([5,9,3,2,1,0,2,3,3,1,0,0])







