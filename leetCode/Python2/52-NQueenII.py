class Solution(object):
    def totalNQueens(self, n):
        self.n = n
        self.board = [-1 for i in xrange(self.n)]
        return self.dfs(0)

    def dfs(self, col_num):
        if col_num == self.n:
            return 1
        res = 0
        for i in xrange(self.n):
            if self.is_queen_valid(col_num, i):
                self.board[col_num] = i
                res += self.dfs(col_num + 1)
        return res

    def is_queen_valid(self, col, row):
        for i in xrange(col):
            if self.board[i] == row or abs(self.board[i] - row) == abs(col - i):
                return False
        return True