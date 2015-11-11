# Time:  O(n)
# Space: O(n)
#
# Clone an undirected graph. Each node in the graph contains a label and a list of its neighbors.
# 
# 
# OJ's undirected graph serialization:
# Nodes are labeled uniquely.
# 
# We use # as a separator for each node, and , as a separator for node label and each neighbor of the node.
# As an example, consider the serialized graph {0,1,2#1,2#2,2}.
# 
# The graph has a total of three nodes, and therefore contains three parts as separated by #.
# 
# First node is labeled as 0. Connect node 0 to both nodes 1 and 2.
# Second node is labeled as 1. Connect node 1 to node 2.
# Third node is labeled as 2. Connect node 2 to node 2 (itself), thus forming a self-cycle.
# Visually, the graph looks like the following:
# 
#        1
#       / \
#      /   \
#     0 --- 2
#          / \
#          \_/
#
# Definition for a undirected graph node

# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []


# Chris:TODO::please write this program again by yourself.

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if node is None:
           return node
        return self.bfs(node, {})

    def dfs(self, node, table):
        if table.get(node) is not None:
           return table[node]
        next_node = UndirectedGraphNode(node.label)
        table[node] = next_node
        for neighbor in node.neighbors:
            next_node.neighbors.append(self.dfs(neighbor, table))
        return next_node

    def bfs(self, node, table):
        queue = [node]
        newhead = UndirectedGraphNode(node.label)
        table[node] = newhead
        while queue:
              curr_node = queue.pop()
              for neighbor in curr_node.neighbors:
                  if table.get(neighbor) is None:
                     new_node = UndirectedGraphNode(neighbor.label)
                     table[curr_node].neighbors.append(new_node)
                     table[neighbor] = new_node
                     queue.append(neighbor)
                  else:
                     table[curr_node].neighbors.append(table[neighbor])
        return newhead



