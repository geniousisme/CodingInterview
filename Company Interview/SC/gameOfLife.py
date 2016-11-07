class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        row_num = len(board)
        col_num = len(board[0])

        for i in xrange(row_num):
            for j in xrange(col_num):
                count = 0

                for I in xrange(max(i - 1, 0), min(i + 2, row_num)):
                    for J in xrange(max(j - 1, 0), min(j + 2, col_num)):
                        count += board[I][J] & 1

                if (count == 4 and board[i][j]) or count == 3:
                    board[i][j] |= 2

        for i in xrange(row_num):
            for j in xrange(col_num):
                board[i][j] >>= 1