class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        ret = []
        grid = [['.']*n for _ in xrange(n)]
        col = [0] * n
        left_diag = [0] * (2*n-1)
        right_diag = [0] * (2*n-1)

        stack = []
        r = 0
        j = 0
        while 1:
            if r < n and j < n:
                if not col[j] and not left_diag[r+j] and not right_diag[n-1-r+j]:
                    grid[r][j] = 'Q'
                    col[j] = 1
                    left_diag[r+j] = 1
                    right_diag[n - 1 - r + j] = 1
                    stack.append(j)
                    j = 0
                    r += 1
                else:
                    j += 1
            else:
                if r == n:
                    ret.append([''.join(row) for row in grid])
                if not stack:
                    break
                r -= 1
                j = stack.pop()
                grid[r][j] = '.'
                col[j] = 0
                left_diag[r+j] = 0
                right_diag[n - 1 - r + j] = 0
                j += 1
        return ret

s = Solution()
print s.solveNQueens(4)
print s.solveNQueens(8)