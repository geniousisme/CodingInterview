# Time:  O(m * n)
# Space: O(1)

# According to the Wikipedia's article: 
# "The Game of Life, also known simply as Life, 
# is a cellular automaton devised by the British 
# mathematician John Horton Conway in 1970."
#
# Given a board with m by n cells, each cell has 
# an initial state live (1) or dead (0). 
# Each cell interacts with its eight neighbors
# (horizontal, vertical, diagonal)
# using the following four rules 
# (taken from the above Wikipedia article):
#
# - Any live cell with fewer than two live neighbors dies,
#   as if caused by under-population.
# - Any live cell with two or three live neighbors lives 
#   on to the next generation.
# - Any live cell with more than three live neighbors dies,
#   as if by over-population..
# - Any dead cell with exactly three live neighbors 
#   becomes a live cell, as if by reproduction.
#
# Write a function to compute the next state 
# (after one update) of the board given its current state.
#
# Follow up: 
# - Could you solve it in-place? Remember that the board needs
#   to be updated at the same time: You cannot update some cells
#   first and then use their updated values to update other cells.
# - In this question, we represent the board using a 2D array. 
#   In principle, the board is infinite, which would cause problems
#   when the active area encroaches the border of the array.
#   How would you address these problems?
#

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