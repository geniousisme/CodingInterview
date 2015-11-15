# Time:  O(n)
# Space: O(h)
#
# Given a binary tree, imagine yourself standing on the right side of it,
# return the values of the nodes you can see ordered from top to bottom.
#
# For example:
# Given the following binary tree,
#    1            <---
#  /   \
# 2     3         <---
#  \     \
#   5     4       <---
# You should return [1, 3, 4].
#


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution1:
    # @param {TreeNode} root
    # @return {integer[]}
    def rightSideView(self, root):
        nodes = []
        self.levelTraversal(root, 0, nodes)
        return [node[0] for node in nodes]

    def levelTraversal(self, root, level, nodes):
        if root:
           if len(nodes) <= level:
              nodes.append([])
           nodes[level].append(root.val)
           self.levelTraversal(root.right, level + 1, nodes)
           self.levelTraversal(root.left,  level + 1, nodes)
        return

class Solution2(object): # recursive solution, dfs
    '''
    TC: O(n)
    SC: O(h), h is the height of the tree
    '''
    def rightSideView(self, root):
        res = []
        self.right_side_view_helper(1, res)
        return res

    def right_side_view_helper(self, root, depth, res):
        if root:
            if depth > len(res):
                res.append(root.val)
            self.right_side_view_helper(root.right, depth + 1, res)
            self.right_side_view_helper(root.left,  depth + 1, res)
        return

class Solution(object): # iterative solution, bfs
    # @param root, a tree node
    # @return a list of integers
    '''
    TC: O(n)
    SC: O(n)
    '''
    def rightSideView(self, root):
        res = []
        if root:
            queue = [root]
            while queue:
                qsize = len(queue)
                for i in xrange(qsize):
                    top = queue.pop(0)
                    if i == 0:
                        res.append(top.val)
                    if top.right:
                        queue.append(top.right)
                    if top.left:
                        queue.append(top.left)
        return res

if __name__ == '__main__':
   s = Solution()

   test = TreeNode(1)
   test.left = TreeNode(2)
   test.right = TreeNode(3)
   test.left.right = TreeNode(5)
   test.left.left = TreeNode(4)
   test.right.left = TreeNode(6)
   test.right.right = TreeNode(7)
   print s.rightSideView(test)
