class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def _my_find_path(root, target, path, cur_sum):
    if not root:
        return
    path.append(root.val)
    cur_sum += root.val

    if cur_sum == target:
        # print
        print '->'.join(map(str, path))
        path.pop()
        return

    if cur_sum > target:
        path.pop()
        return

    _my_find_path(root.left, target, path, cur_sum)
    _my_find_path(root.right, target, path, cur_sum)
    path.pop()


def print_path(root, target):
    _my_find_path(root, target, [], 0)


a1 = Node(1)
a2 = Node(9)
a3 = Node(3)
a4 = Node(7)
a5 = Node(2)

a1.left = a2
a2.left = a3
a1.right = a4
a4.right = a5

# print_path(a1, 8)




class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y


def dfs(grid, i, j, d_i, d_j, step, max_height, visited):
    if i == d_i and j == d_j:
        return max_height + step

    if not visited[i][j]:
        return visited[i][j]

    m, n = len(visited), len(visited[0])
    visited[i][j] = 1

    # update max_height
    max_height = max(max_height, grid[i][j])

    res = float.inf
    for x, y in ((i+1, j), (i-1, j), (i, j+1), (i, j-1)):
        if 0 <= x < m and 0 <= y < n and not visited[x][y]:
            res = min(res, dfs(grid, x, y, d_i, d_j, step+1, max_height, visited))

    visited[i][j] = res
    return res




def shortest_path(grid, start, end):
    if not grid or not grid[0]:
        return 0

    m, n = len(grid), len(grid[0])

    visited = [[0]*n for _ in xrange(m)]
    return dfs(grid, start.x, start.y, end.x, end.y, 0, grid[start.x][start.y], visited)







