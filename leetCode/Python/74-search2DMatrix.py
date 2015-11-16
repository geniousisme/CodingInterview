# Time:  O(logm + logn)
# Space: O(1)
#
# Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:
# 
# Integers in each row are sorted from left to right.
# The first integer of each row is greater than the last integer of the previous row.
# For example,
# 
# Consider the following matrix:
# 
# [
#   [1,   3,  5,  7],
#   [10, 11, 16, 20],
#   [23, 30, 34, 50]
# ]
# Given target = 3, return true.
#

class Solution1:
    # @param {integer[][]} matrix
    # @param {integer} target
    # @return {boolean}
    def searchMatrix(self, matrix, target): # recursive version
        row_num = len(matrix)
        col_num = len(matrix[0])
        sorted_1D_list = []
        for i in xrange(row_num):
            sorted_1D_list.extend(matrix[i])
        return self.binarySearch(sorted_1D_list, 0, row_num * col_num, target)

    def binarySearch(self, nums, start, end, target):
        if len(nums[start:end]) == 1:
           return nums[start] == target
        mid = (end + start) / 2
        if target > nums[mid]:
           return self.binarySearch(nums, mid, end, target)
        elif target < nums[mid]:
             return self.binarySearch(nums, start, mid, target)
        else: # target == nums[mid]
             return True

class Solution(object):
    def searchMatrix(self, matrix, target):
        if not matrix:
            return False
        if not matrix[0]:
            return False
        row_num = len(matrix)
        col_num = len(matrix[0])
        start = 0; end = row_num * col_num - 1
        while start + 1 < end:
            mid = (start + end) / 2
            x, y = mid / col_num, mid % col_num
            if matrix[x][y] == target:
                return True
            elif matrix[x][y] > target:
                end = mid
            else:
                start = mid
        if matrix[start / col_num][start % col_num] == target:
            return True
        if matrix[end / col_num][end % col_num] == target:
            return True
        return False


if __name__ == '__main__':
   s = Solution()
   matrix = [                   \
              [1,   3,  5,  7], \
              [10, 11, 16, 20], \
              [23, 30, 34, 50]  \
            ]
   print s.searchMatrix(matrix, 3)
   print s.searchMatrix(matrix, 70)
   print s.searchMatrix(matrix, 0)
   print s.searchMatrix(matrix, 30)


