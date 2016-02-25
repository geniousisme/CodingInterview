# Time:  O(m * n)
# Space: O(m * n)
#
# Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. 
# An island is surrounded by water and is formed by connecting adjacent lands horizontally 
# or vertically. You may assume all four edges of the grid are all surrounded by water.
#
# Example 1:
#
# 11110
# 11010
# 11000
# 00000
# Answer: 1
#
# Example 2:
#
# 11000
# 11000
# 00100
# 00011
# Answer: 3
#

class Solution1:
    # @param {character[][]} grid
    # @return {integer}
    def __init__(self):
        self.length = self.width = 0
        self.visited = []

    def numIslands(self, grid):
        if not grid: return 0
        self.length = len(grid[0])
        self.width  = len(grid)
        self.visited = [[False for i in xrange(self.length)] for j in xrange(self.width)]
        queue = []
        count = 0
        for i in xrange(self.length):
            for j in xrange(self.width):
                if grid[i][j] == '1' and not self.visited[i][j]:
                   queue.insert(0, (i, j))
                   self.bfs(grid, queue)
                   count += 1
                else:
                   self.visited[i][j] = True
        return count

    def bfs(self, grid, queue):
        while queue:
              x, y = queue.pop()
              # if x >= self.length - 1 or y >= self.width - 1:
              #    continue
              self.visited[x][y] = True
              if grid[x][y] == '1':
                 # grid[x][y] = 2
                 if x + 1 < self.length:
                    queue.insert(0, (x + 1, y))
                 if x - 1 > -1:
                    queue.insert(0, (x - 1, y))
                 if y + 1 < self.width:
                    queue.insert(0, (x, y + 1))
                 if y - 1 > -1:
                    queue.insert(0, (x, y - 1))


    def print_matrix(self, matrix):
        for i in xrange(len(matrix)):
            print ' '.join([n for n in matrix[i]])


class Solution2:
    # @param grid, a list of list of characters
    # @return an integer
    def numIslands(self, grid):
        ans = 0
        if not len(grid):
            return ans
        m, n = len(grid), len(grid[0])
        visited = [ [False] * n for x in range(m) ] # m * n
        for x in range(m):
            for y in range(n):
                if grid[x][y] == '1' and not visited[x][y]:
                    ans += 1
                    self.bfs(grid, visited, x, y, m, n)
        return ans

    def bfs(self, grid, visited, x, y, m, n):
        dz = zip( [1, 0, -1, 0], [0, 1, 0, -1] )
        queue = [ (x, y) ]
        visited[x][y] = True
        while queue:
            front = queue.pop(0)
            for p in dz:
                np = (front[0] + p[0], front[1] + p[1])
                if self.isValid(np, m, n) and grid[np[0]][np[1]] == '1' and not visited[np[0]][np[1]]:
                    visited[ np[0] ][ np[1] ] = True
                    queue.append(np)

    def isValid(self, np, m, n):
        return np[0] >= 0 and np[0] < m and np[1] >= 0 and np[1] < n

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

if __name__ == '__main__':
   s = Solution()
   grid = [            \
           ['11110'],\
           [1,1,0,1,0],\
           [1,1,0,0,1],\
           [1,1,1,1,0],\
           [0,0,1,0,1] \
          ]
   print s.numIslands(grid)
   s.print_matrix(grid)
        





