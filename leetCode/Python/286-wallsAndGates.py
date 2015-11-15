# You are given a m x n 2D grid initialized with these three possible values.

# -1 - A wall or an obstacle.
# 0 - A gate.
# INF - Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than2147483647.
# Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.

# For example, given the 2D grid:

# INF  -1  0  INF
# INF INF INF  -1
# INF  -1 INF  -1
#   0  -1 INF INF

#  After running your function, the 2D grid should be:

#   3  -1   0   1
#   2   2   1  -1
#   1  -1   2  -1
#   0  -1   3   4

from collections import deque

class Solution(object):
    def wallsAndGates(self, rooms):
        """
        TC: O(m * n)
        SC: O(g)

        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.
        """
        INF = 2147483647
        dq = deque([(i, j) for i, row in enumerate(rooms) for j, room in enumerate(row) if not room])
        while dq:
            (i, j) = dq.popleft()
            for I, J in (i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1):
                if -1 < I < len(rooms) and -1 < J < len(rooms[0]) and rooms[I][J] == INF:
                    rooms[I][J] = rooms[i][j] + 1
                    dq.append((I, J))

if __name__ == "__main__":
    s = Solution()
    INF = 2147483647
    rooms =                  \
    [                        \
        [INF, -1,  0,   INF],\
        [INF, INF, INF,  -1],\
        [INF, -1,  INF,  -1],\
        [0,   -1,  INF, INF] \
    ]
    s.wallsAndGates(rooms)
    print rooms


