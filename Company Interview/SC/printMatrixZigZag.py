class Solution(object):
    # @param: a matrix of integers
    # @return: a list of integers
    def printZMatrix(self, matrix):
        if not matrix:
            return None
        col_num = len(matrix)
        row_num = len(matrix[0])
        m = col_num - 1
        n = row_num - 1
        result = []
        for i in xrange(m + n + 1):
            if i % 2 == 0:
                for x in xrange(i, -1, -1):
                    if x <= m and i - x <= n:
                        result.append(matrix[x][i - x])
            else:
                for x in xrange(0, i + 1, 1):
                    if x <= m and i - x <= n:
                        result.append(matrix[x][i - x])
        return result

if __name__ == "__main__":
    s = Solution()
    print s.printZMatrix(
        [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12]
        ]
    )

