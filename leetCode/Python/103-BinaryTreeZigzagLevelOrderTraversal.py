'''
Given a binary tree, return the zigzag level order traversal of its nodes' values. 
(ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree {3,9,20,#,#,15,7},
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution1(object): # DFS solution
    def __init__(self):
        self.res = []

    def zigzagLevelOrder(self, root):
        """
        Time:  O(n)
        Space: O(n)
        """
        if self.res:
            self.res = []
        if root:
            self.zigzag_level_helper(root, 0)
        return self.res

    def zigzag_level_helper(self, root, depth):
        if root is None:
            return
        if len(self.res) < depth + 1:
            self.res.append([])
        if depth % 2 == 0:
            self.res[depth].append(root.val)
        else:
            self.res[depth].insert(0, root.val)
        self.zigzag_level_helper(root.left, depth + 1)
        self.zigzag_level_helper(root.right, depth + 1)

class Solution(object): # BFS solution
    def zigzagLevelOrder(self, root):
        res = []; queue = []
        if root:
            queue.append((0, root))
            while queue:
                depth, root = queue.pop()
                if root is None:
                    continue
                if len(res) < depth + 1:
                    res.append([])
                if depth % 2 == 1:
                    res[depth].append(root.val)
                else:
                    res[depth].insert(0, root.val)
                queue.append((depth + 1, root.left))
                queue.append((depth + 1, root.right))
        return res





if __name__ == '__main__':
   test             = TreeNode(1)
   test.left        = TreeNode(2)
   test.right       = TreeNode(3)
   test.left.left   = TreeNode(4)
   test.left.right   = TreeNode(-1)
   test.right.left  = TreeNode(-1)
   test.right.right = TreeNode(5)
   print Solution().zigzagLevelOrder(test)

