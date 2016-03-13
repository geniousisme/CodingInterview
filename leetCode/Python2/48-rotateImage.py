class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        width = length = len(matrix)
        for i in xrange(width):
            for j in xrange(i + 1, length): # notice: i + 1 to avoid flip elem again!
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in xrange(width):
            matrix[i].reverse()


