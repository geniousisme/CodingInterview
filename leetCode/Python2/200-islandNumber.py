class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        self.row_num = len(grid)
        self.col_num = len(grid[0])
        count        = 0
        visited = [[False for j in xrange(self.col_num)] for i in xrange(self.row_num)]

        for i in xrange(self.row_num):
            for j in xrange(self.col_num):
                if not visited[i][j] and grid[i][j] == '1':
                    self.dfs(grid, visited, i, j)
                    count += 1
        return count

    def dfs(self, grid, visited, x, y):
        if visited[x][y] or grid[x][y] == '0':
            return
        visited[x][y] = True
        if x != 0:
            self.dfs(grid, visited, x - 1, y)
        if x != self.row_num - 1:
            self.dfs(grid, visited, x + 1, y)
        if y != 0:
            self.dfs(grid, visited, x, y - 1)
        if y != self.col_num - 1:
            self.dfs(grid, visited, x, y + 1)

if __name__ == "__main__":
    s = Solution()
    grid = ["10"]
    print s.numIslands(grid)