import collections


# Time:  O(m * n * l), A is m x n matrix, B is n x l matrix
# Space: O(m * l)

class Solution(object):
    def multiply(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        if not A or not B:
            return []
        m, n, l = len(A), len(A[0]), len(B[0])
        res = [[0 for _ in xrange(l)] for _ in xrange(m)]
        for i in xrange(m):
            for j in xrange(n):
                if A[i][j]:
                    for k in xrange(l):
                        res[i][k] += A[i][j] * B[j][k]
        return res


class Solution1(object): # too slow!
    def multiply(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        if not A or not B:
            return []
        dictA = self.get_non_zero_dict(A)
        dictB = self.get_non_zero_dict(B)
        res_dict   = collections.defaultdict(int)
        for ai, aj in dictA:
            for bi, bj in dictB:
                if aj == bi:
                    res_dict[(ai, bj)] += dictA[(ai, aj)] * dictB[(bi, bj)]
        res_matrix = [[0 for _ in xrange(len(B[0]))] for _ in xrange(len(A))]
        for i in xrange(len(A)):
            for j in xrange(len(B[0])):
                if res_dict.get((i, j)) is not None:
                    res_matrix[i][j] = res_dict[(i, j)]
        return res_matrix

    def get_non_zero_dict(self, matrix):
        dict = {}
        for i in xrange(len(matrix)):
            for j in xrange(len(matrix[0])):
                if matrix[i][j]:
                    dict[(i, j)] = matrix[i][j]
        return dict

if __name__ == "__main__":
    s = Solution()
    A = [[1, 0, 0], [-1, 0, 3]]
    B = [[7, 0, 0], [0, 0, 0], [0, 0, 1]]
    print s.multiply(A, B)