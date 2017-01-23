from collections import defaultdict


class Solution(object):
    def __init__(self):
        self.jump = defaultdict(dict)
        for start, end, p in ((1,3,2), (4,6,5), (7,9,8), (1,7,4), (2,8,5), (3,9,6), (1,9,5), (3,7,5)):
            self.jump[start][end] = p
            self.jump[end][start] = p

    def numberOfPatterns(self, m, n):
        visited = [0] * 10
        res = 0

        def dfs(i, step):
            if step == 1:
                return 1
            visited[i] = 1
            ret = sum(dfs(n, step-1) for n in xrange(1, 10) if not visited[n] and
                      ((i not in self.jump or n not in self.jump[i]) or visited[self.jump[i][n]]))
            visited[i] = 0
            return ret

        for step in xrange(max(1,m), min(n + 1,10)):
            res += dfs(1, step) * 4
            res += dfs(2, step) * 4
            res += dfs(5, step)
        return res

s = Solution()
print s.numberOfPatterns(1,2)