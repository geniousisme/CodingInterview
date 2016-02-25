# Time:  O(n)
# Space: O(1)
#
# Given a binary tree, return the inorder traversal of its nodes' values.
#
# For example:
# Given binary tree {1,#,2,3},
#   1
#    \
#     2
#    /
#   3
# return [1,3,2].
#
# Note: Recursive solution is trivial, could you do it iteratively?
#


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class MorrisSolution(object):
    # @param root, a tree node
    # @return a list of integers
    '''
    TC: O(n)
    SC: O(1)
    '''
    def inorderTraversal(self, root):
        curr = root; prev = None; res = []
        while curr:
            if curr.left is None:
                res.append(curr.val)
                curr = curr.right
            else:
                prev = curr.left
                while prev.right and prev.right != curr:
                    prev = prev.right

                if prev.right is None:
                    prev.right = curr
                    curr = curr.left
                else:
                    res.append(curr.val)
                    prev.right = None
                    curr = curr.right
        return res

class Solution(object):
    # @param {TreeNode} root
    # @return {integer[]}
    '''
    TC: O(n)
    SC: O(n)
    '''
    def __init__(self):
        self.stack = []
        self.res   = []

    def inorderTraversal(self, root):
        self.recursive_traverse(root)
        return self.res

    def recursive_traverse(self, node): # recursive
        if node:
           self.recursive_traverse(node.left)
           self.res.append(node.val)
           self.recursive_traverse(node.right)
        return

    def iterTraverse(self, root): # iterative
        while root or self.stack:
              if root:
                 self.stack.append(root)
                 root = root.left
              else:
                 root = self.stack.pop()
                 self.res.append(root.val)
                 root = root.right
        return
if __name__ == "__main__":
    ms = MorrisSolution()
    t1 = TreeNode(1)
    t2 = TreeNode(2)
    t3 = TreeNode(3)
    t4 = TreeNode(4)
    t5 = TreeNode(5)
    t6 = TreeNode(6)
    t7 = TreeNode(7)
    t1.left = t2
    t1.right = t3
    t2.left = t4
    t2.right = t5
    t3.left = t6
    t3.right = t7
    print ms.inorderTraversal(t1)