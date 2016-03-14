'''
Given an array of non-negative integers, 
you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

For example:
Given array A = [2,3,1,1,4]

The minimum number of jumps to reach the last index is 2. 
(Jump 1 step from index 0 to 1, then 3 steps to the last index.)

Note:
You can assume that you can always reach the last index.

Subscribe to see which companies asked this question
'''

class Solution(object):
    # @param {integer[]} nums
    # @return {boolean}
    def jump(self, nums):
        length = len(nums)
        last = curr = step_num = 0
        for i in xrange(length):
            print 'i:', i
            print 'last:', last
            print 'curr:', curr
            if i > last:
               print '###'
               last = curr
               print 'last:', last
               print '###'
               step_num += 1
            if i + nums[i] > curr:
               curr = i + nums[i]
        return step_num

class Solution(object):
    def jump(self, nums):
        length = len(nums)
        last_idx = curr_idx = step_count = 0
        for i in xrange(length):
            if i > last_idx:
                last_idx = curr_idx
                step_count += 1
            if i + nums[i] >= curr_idx:
                curr_idx = i + nums[i]
        return step_count

if __name__ == '__main__':
   s = Solution()
   # print s.jump([2,3,1,1,4])
   print s.jump([2, 2, 2, 1, 4])
   # print s.jump([1, 1, 1, 1, 2, 0, 0])
   # print s.jump([3, 2, 1, 0, 4])
   # print s.jump([5,9,3,2,1,0,2,3,3,1,0,0])







