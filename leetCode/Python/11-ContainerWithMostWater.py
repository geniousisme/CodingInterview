# Time:  O(n)
# Space: O(1)
#
# Given n non-negative integers a1, a2, ..., an,
# where each represents a point at coordinate (i, ai).
# n vertical lines are drawn such that the two endpoints of
# line i is at (i, ai) and (i, 0). Find two lines,
# which together with x-axis forms a container,
# such that the container contains the most water.
#
# Note: You may not slant the container.
#

class Solution1:
    # @return an integer
    def maxArea(self, height):
        left = max_area = 0; right = len(height) - 1
        while left != right:
              tmp_area = min(height[left], height[right]) * (right - left)
              if tmp_area > max_area:
                 max_area = tmp_area
              if height[left] < height[right]:
                 left  += 1
              else:
                 right -= 1
        return max_area


class Solution(object):
    # @return an integer
    def maxArea(self, height):
        max_area, i, j = 0, 0, len(height) - 1
        while i < j:
            max_area = max(max_area, min(height[i], height[j]) * (j - i))
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return max_area


# from maxArea import Solution
# s = Solution()
# s.maxArea([1,2,3,4]) 
# s.maxArea([2,2,3,6]) 