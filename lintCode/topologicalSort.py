# Definition for a Directed graph node
class DirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class Solution:
    """
    @param graph: A list of Directed graph node
    @return: A list of integer
    """
    def dfs(self, graph_node, res, node_count, graph):
        res.append(graph_node.label)
        if node_count.get(graph_node, 0) != 0:
            node_count[graph_node] -= 1
        for j in xrange(len(graph_node.neighbors)):
            node_count[graph_node.neighbors[j]] -= 1
            if node_count[graph_node.neighbors[j]] == 0:
                self.dfs(graph_node.neighbors[j], res, node_count, graph)

    def topSort(self, graph):
        res = []
        node_count = {}
        graph_size = len(graph)
        for i in xrange(graph_size):
            for j in xrange(len(graph[i].neighbors)):
                if node_count.get(graph[i].neighbors[j]):
                    node_count[graph[i].neighbors[j]] += 1
                else:
                    node_count[graph[i].neighbors[j]] = 1

        for i in xrange(graph_size):
            if node_count.get(graph[i], 0) == 0:
                self.dfs(graph[i], res, node_count, graph)
        return res

if __name__ == "__main__":
    s = Solution()
    dg0 = DirectedGraphNode(0)
    dg1 = DirectedGraphNode(1)
    dg2 = DirectedGraphNode(2)
    dg3 = DirectedGraphNode(3)
    dg4 = DirectedGraphNode(4)
    dg5 = DirectedGraphNode(5)
    dg0.neighbors = [dg1, dg2, dg3]
    dg1.neighbors = [dg4]
    dg2.neighbors = [dg4, dg5]
    dg3.neighbors = [dg4, dg5]
    graph = [dg0, dg1, dg2, dg3, dg4, dg5]
    print s.topSort(graph)







