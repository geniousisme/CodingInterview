class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class Solution(object):
    def cloneGraph(self, node):
        if node is None:
            return node
        return self.bfs(node, {})

    def dfs(self, node, table):
        if table.get(node) is not None:
            return table[node]
        new_node = UndirectedGraphNode(node.label)
        table[node] = new_node
        for neighbor in node.neighbors:
            new_node.neighbors.append(self.dfs(neighbor, table))
        return new_node # notice, remember to return things back!

    def bfs(self, node, table):
        queue = [node]
        new_node = UndirectedGraphNode(node.label)
        table[node] = new_node
        while queue:
            curr_node = queue.pop()
            for neighbor in curr_node.neighbors:
                if table.get(neighbor) is not None:
                    table[curr_node].neighbors.append(table[neighbor])
                else:
                    neighbor_node = UndirectedGraphNode(neighbor.label)
                    table[neighbor] = neighbor_node
                    table[curr_node].neighbors.append(neighbor_node)
                    queue.append(neighbor)
        return new_node

