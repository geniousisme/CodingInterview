#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 1. flood fill。感谢地里面经：here and here and here
# 就上面题目的各种变种，题目是有一个矩阵
# 1代表已经染色，0代表没有染色。
# 完成一个函数，
# 输入：矩阵a，整数x， 整数y
# 输出:
# 返回一个矩阵，为以(x,y)点（0-based）为开始点的染色结果，
# 将其周围区域染色，直到遇到已经染色的位置或边界为止
# 若(x, y)已经染色则直接返回。注意：只能向上下左右四个方向染色。
# 输入样例：
# 111111
# 111001
# 100110
# (2, 1)

# 输出样例：
# 111111
# 111001
# 111110

class Solution(object): # dfs
    '''
    Time:  O(m * n)
    Space: O(1)
    '''
    def floodFill(self, matrix, x, y):
        if not matrix or x is None or y is None:
            return
        self.flood_fill_helper(matrix, x, y)

    def flood_fill_helper(self, matrix, x, y):
        if x < 0 or x >= len(matrix) or y < 0 or y >= len(matrix[0]) or matrix[x][y] != 0:
            return
        matrix[x][y] = 1
        self.flood_fill_helper(matrix, x + 1, y)
        self.flood_fill_helper(matrix, x - 1, y)
        self.flood_fill_helper(matrix, x, y + 1)
        self.flood_fill_helper(matrix, x, y - 1)

class Solution2(object): # bfs
    '''
    Time:  O(m * n)
    Space: O(1)
    '''
    def floodFill(self, matrix, x, y):
        if not matrix:
            return
        queue = [(x, y)]
        while queue:
            x, y = queue.pop(0)
            if x < 0 or x >= len(matrix) or y < 0 or y >= len(matrix[0]) or matrix[x][y] != 0:
                continue
            matrix[x][y] = 1
            queue.append((x + 1, y))
            queue.append((x - 1, y))
            queue.append((x, y + 1))
            queue.append((x, y - 1))

if __name__ == "__main__":
    s2 = Solution2()
    matrix = [[1, 1, 1, 1, 1, 1], [1, 1, 1, 0, 0, 1], [1, 0, 0, 1, 1, 0]]
    s2.floodFill(matrix, 2, 1)
    for i in xrange(len(matrix)):
        print matrix[i]
