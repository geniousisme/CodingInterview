# Time:  O(n^2)
# Space: O(1)
#
# Given an array S of n integers,
# find three integers in S such that the sum is closest to a given number, target.
# Return the sum of the three integers.
# You may assume that each input would have exactly one solution.
#
# For example, given array S = {-1 2 1 -4}, and target = 1.
#
# The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
#


class Solution:
    # @return an integer
    # in this algo, we search all the sum comb to find the smallest diff between sum and target
    # kind of like 3Sum, but just modify the process a little.
    # Calculate the diff everytime, if equals to target, then you can return
    # if it is bigger than target, then we need to move the right ptr backward
    # if it is smaller than target, then we need to move the left ptr forward
    def threeSumClosest(self, num_list, target):
        num_list = sorted(num_list)
        diff     = 2 ** 31 - 1; sum = 0
        for i in xrange(len(num_list)):
            left = i + 1; right = len(num_list) - 1
            while right > left:
                  tmp_sum = num_list[i] + num_list[left] + num_list[right]
                  tmp_diff = abs(target - tmp_sum)
                  if tmp_diff == 0:
                     return tmp_sum
                  if diff > tmp_diff:
                     diff = tmp_diff
                     sum  = tmp_sum
                  if tmp_sum > target:
                     right -= 1
                  if tmp_sum < target:
                     left += 1
        return sum

if __name__ == '__main__':
   s = Solution()
   print s.threeSumClosest([-1, 2, 1, -4], 1)
   