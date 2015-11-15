# Time:  O(m * n)
# Space: O(1)
#
# Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place.
#
# Follow up:
# Did you use extra space?
# A straight forward solution using O(mn) space is probably a bad idea.
# A simple improvement uses O(m + n) space, but still not the best solution.
# Could you devise a constant space solution?
#


class Solution1:
    # @param {integer[][]} matrix
    # @return {void} Do not return anything, modify matrix in-place instead.
    '''
    TC: O(m * n)
    SC: O(m + n)
    '''
    def setZeroes(self, matrix):
        row_num = len(matrix)
        col_num = len(matrix[0])
        row_idx_list = [False] * row_num 
        col_idx_list = [False] * col_num
        for i in xrange(row_num):
            for j in xrange(col_num):
                if not matrix[i][j]:
                   row_idx_list[i] = True
                   col_idx_list[j] = True
        for i in xrange(row_num):
            if row_idx_list[i]:
               matrix[i] = [0] * col_num
        for j in xrange(col_num):
            if col_idx_list[j]:
               for i in xrange(row_num):
                   matrix[i][j] = 0

    def print_matrix(self, matrix):
        for i in xrange(len(matrix)):
            print ' '.join([ str(n) for n in matrix[i]])


class Solution(object):
    # @param matrix, a list of lists of integers
    # RETURN NOTHING, MODIFY mat
    '''
    TC: O(m * n)
    SC: O(1)
    '''
    def setZeroes(self, matrix):
        # check first column with 0 or not
        first_col = reduce(lambda acc, i: acc or matrix[i][0] == 0, xrange(len(matrix)), False)
        # check first row with 0 or not
        first_row = reduce(lambda acc, j: acc or matrix[0][j] == 0, xrange(len(matrix[0])), False)

        # solve the internal matrix first, leave the first row an first column left
        for i in xrange(1, len(matrix)):
            for j in xrange(1, len(matrix[0])):
                # if matrix[i][j] == 0, make matrix[i][0] & matrix[0][j] zero, use them to decide
                if matrix[i][j] == 0:
                    matrix[i][0], matrix[0][j] = 0, 0
        # if we want to make ith row or jth column zero or not
        for i in xrange(1, len(matrix)):
            for j in xrange(1, len(matrix[0])):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # At the end, check if matrix[i][0] equals to zero if first_col contains zero
        if first_col:
            for i in xrange(len(matrix)):
                matrix[i][0] = 0
        # check matrix[0][j] equals to zero if first_row contains zero
        if first_row:
            for j in xrange(len(matrix[0])):
                matrix[0][j] = 0

if __name__ == '__main__':
   s = Solution()
   matrix = [[3, 4, 5, 9], [8, 0, 0, 1], [1, 7, 1, 9]]
   s.print_matrix(matrix)
   s.setZeroes(matrix)
   s.print_matrix(matrix)