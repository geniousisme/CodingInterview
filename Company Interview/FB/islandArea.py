#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 给定matrix，只有0和1，求1的连通size
# 连通只算上下左右，不算对角线。比如：

# 0 1 0 0 1
# 1 1 1 0 0
# 1 0 0 0 1
# 0 0 0 0 1

# 返回 5， 1， 2

class Solution(object): # dfs
    '''
    Time:  O(m * n)
    Space: O(m * n)
    '''
    def islandArea(self, matrix):
        self.visited = [[False for _ in xrange(len(matrix[0]))] for _ in xrange(len(matrix))]
        for i in xrange(len(matrix)):
            for j in xrange(len(matrix[0])):
                if matrix[i][j] == 1 and not self.visited[i][j]:
                    self.area = 0
                    self.island_area_helper(matrix, i, j)
                    print self.area

    def island_area_helper(self, matrix, x, y):
        if x < 0 or x >= len(matrix) or y < 0 or y >= len(matrix[0])           \
            or matrix[x][y] != 1 or self.visited[x][y]:
            return
        self.visited[x][y] = True
        self.area += 1
        self.island_area_helper(matrix, x + 1, y)
        self.island_area_helper(matrix, x - 1, y)
        self.island_area_helper(matrix, x, y + 1)
        self.island_area_helper(matrix, x, y - 1)

class Solution2(object): # bfs
    '''
    Time:  O(m * n)
    Space: O(m * n)
    '''
    def islandArea(self, matrix):
        visited = [[False for _ in xrange(len(matrix[0]))] for _ in xrange(len(matrix))]
        for i in xrange(len(matrix)):
            for j in xrange(len(matrix[0])):
                if not visited[i][j] and matrix[i][j] == 1:
                    print self.island_area_helper(matrix, visited, i, j)

    def island_area_helper(self, matrix, visited, x, y):
        queue = [(x, y)]
        area  = 0
        while queue:
            x, y = queue.pop(0)
            if x < 0 or x >= len(matrix) or y < 0 or y >= len(matrix[0]) or matrix[x][y] != 1 or visited[x][y]:
                continue
            visited[x][y] = True
            area += 1
            queue.append((x + 1, y))
            queue.append((x - 1, y))
            queue.append((x, y + 1))
            queue.append((x, y - 1))
        return area

if __name__ == "__main__":
    s2 = Solution2()
    matrix = [[0, 1, 0, 0, 1], [1, 1, 1, 0, 0], [1, 0, 0, 0, 1], [0, 0, 0, 0, 1]]
    s2.islandArea(matrix)
