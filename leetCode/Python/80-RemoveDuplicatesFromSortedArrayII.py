# Time:  O(n)
# Space: O(1)
#
# Follow up for "Remove Duplicates":
# What if duplicates are allowed at most twice?
# 
# For example,
# Given sorted array A = [1,1,1,2,2,3],
# 
# Your function should return length = 5, and A is now [1,1,2,2,3].
#

class Solution1:
    # @param {integer[]} nums
    # @return {integer}
    def myselfRemoveDuplicates(self, nums): # with ordered list
        i = 0; prev = None; last = len(nums) - 1; repeat_len = 0
        # appeared_times = 0
        while i <= last:
              if prev != nums[i]:
                 prev = nums[i]
                 appeared_times = 0
                 repeat_len += 1
                 i += 1 
              else:
                 appeared_times += 1
                 if appeared_times == 1:
                    i += 1
                    repeat_len += 1
                 if appeared_times > 1:
                    nums.pop(i)
                    last -= 1
        return repeat_len

    def removeDuplicates(self, nums):
        length = len(nums)
        repeated_times = 1
        prev = 0
        for i in xrange(1, length):
            if nums[i] == nums[i - 1]:
               repeated_times += 1
               if repeated_times <= 2:
                  prev += 1
                  nums[prev] = nums[i]
            else:
               repeated_times = 1
               prev += 1
               nums[prev] = nums[i]
        return prev + 1

class Solution(object):
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if not A:
            return 0

        last, i, same = 0, 1, False
        while i < len(A):
            if A[last] != A[i] or not same:
                same = A[last] == A[i]
                last += 1
                A[last] = A[i]
            i += 1
        print A
        return last + 1

if __name__ == '__main__':
   s = Solution1()
   nums = [1,1,1,1,1,2,2,3,3,3,4,5]
   print s.removeDuplicates(nums)
   # print nums

   nums = [0,0,0,0,0]
   print s.removeDuplicates(nums)
   # print nums

   nums = [0, 1]
   print s.removeDuplicates(nums)
   # print nums

