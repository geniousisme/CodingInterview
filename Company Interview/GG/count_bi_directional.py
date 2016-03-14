class Solution(object):
    '''
    TC: O(N)
    SC: O(N)
    '''
    def count_bi_direct(self, edges):
        edge_dict = {}
        count = 0
        for edge in edges:
            if edge_dict.get((edge[1], edge[0])) is not None:
                count += 1
            else:
                edge_dict[edge] = 1
        return count

    '''
    TC: O(N ^ 2)
    SC: O(1)
    '''
    def count_bi_direct_brute_force(self, edges):
        count = 0
        edges = list(set(edges)) # remove the repeated edges
        for i in xrange(len(edges)):
            for j in xrange(i, len(edges)):
                if edges[i][1] == edges[j][0] and edges[j][1] == edges[i][0]:
                    count += 1
        return count


if __name__ == "__main__":
    s = Solution()
    print s.count_bi_direct([(1, 2), (2, 3), (2, 1)])
    print s.count_bi_direct([(1, 2), (1, 2), (2, 3), (2, 1)])
    print s.count_bi_direct([(1, 2), (2, 1), (2, 3), (3, 2)])
    print s.count_bi_direct_brute_force([(1, 2), (2, 3), (2, 1)])
    print s.count_bi_direct_brute_force([(1, 2), (1, 2), (2, 3), (2, 1)])
    print s.count_bi_direct_brute_force([(1, 2), (2, 1), (2, 3), (3, 2)])

