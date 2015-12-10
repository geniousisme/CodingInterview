import collections

class Solution(object):
    def maxArea(self, matrix):
        if not matrix:
            return 0
        self.row_num = len(matrix); self.col_num = len(matrix[0]); max_area = 0
        self.visited = [[False for _ in xrange(self.col_num)] for _ in xrange(self.row_num)]
        for i in xrange(self.row_num):
            for j in xrange(self.col_num):
                if not self.visited[i][j]:
                    max_area = max(self.max_area_helper(matrix, matrix[i][j], i, j), max_area)
        return max_area

    def max_area_helper(self, matrix, color, x, y):
        queue = collections.deque()
        queue.append((x, y))
        area = 0
        while queue:
            x, y = queue.popleft()
            if x < 0 or x >= self.row_num or y < 0 or y >= self.col_num or self.visited[x][y] or matrix[x][y] != color:
                continue
            area += 1
            self.visited[x][y] = True
            queue.append((x + 1, y))
            queue.append((x - 1, y))
            queue.append((x, y + 1))
            queue.append((x, y - 1))
        return area

if __name__ == "__main__":
    s = Solution()
    matrix = [['G', 'G', 'G', 'G'],
              ['G', 'G', 'B', 'C'],
              ['B', 'B', 'B', 'D'],
              ['E', 'C', 'E', 'D']]
    print s.maxArea(matrix)
