from copy import deepcopy

class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        triangle_path = deepcopy(triangle)
        tmp_triangle = deepcopy(triangle)

        for i in xrange(len(triangle) - 2, -1, -1):
            for j in xrange(i + 1):
                triangle[i][j] += min(triangle[i + 1][j], triangle[i + 1][j + 1])
                triangle_path[i][j] = str(triangle_path[i][j]) + "->"
                if triangle[i + 1][j] < triangle[i + 1][j + 1]:
                    triangle_path[i][j] = triangle_path[i][j] + str(triangle_path[i + 1][j])
                else:
                    triangle_path[i][j] = triangle_path[i][j] + str(triangle_path[i + 1][j + 1])
        return triangle[0][0], triangle_path[0][0]

if __name__ == "__main__":
    s = Solution()
    print s.minimumTotal(
            [
                [2],
                [3, 4],
                [6, 5, 7],
                [4, 1, 8, 3]
            ]
        )