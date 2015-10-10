# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []


# Chris:TODO::please write this program again by yourself.

class Solution1:
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

class Solution(object):
    def cloneGraph(self, node):
        if node is None:
            return node
        return self.dfs(node, {})

    def dfs(self, node, table):
        if table.get(node) is not None:
            return table[node]
        next_node = UndirectedGraphNode(node.label)
        table[node] = next_node # record it as visited
        for n in node.neighbors:
            next_node.neighbors.append(self.dfs(n, table))
        return next_node

    def bfs(self, node, table):
        queue = [node]
        new_head = UndirectedGraphNode(node.label)
        table[node] = new_head
        while queue:
            curr_node = queue.pop()
            for neighbor in curr_node.neighbors:
                # already exist, store it into curr_node neighbors
                if table.get(neighbor) is not None:
                    table[curr_node].neighbors.append(neighbor)
                else:
                    # not exist yet in table, store it into curr_node neighbors
                    # and store it into table as visited.
                    # last part, store it into queue for its neighbors visiting.
                    new_node = UndirectedGraphNode(neighbor.label)
                    table[curr_node].neighbors.append(new_node)
                    table[neighbor] = new_node
                    queue.append(new_node)
        return new_head



