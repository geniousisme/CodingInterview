# Time:  O(n)
# Space: O(1)
#
# Given a binary tree, return the preorder traversal of its nodes' values.
#
# For example:
# Given binary tree {1,#,2,3},
#    1
#     \
#      2
#     /
#    3
# return [1,2,3].
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
    '''
    TC: O(n)
    SC: O(1)
    '''
    def preorderTraversal(self, root):
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
                    res.append(curr.val)
                    prev.right = curr
                    curr = curr.left
                else:
                    prev.right = None
                    curr = curr.right
        return res

class Solution:
    # @param {TreeNode} root
    # @return {integer[]}
    '''
    TC: O(n)
    SC: O(1)
    '''
    def preorderTraversal(self, root):
        res = []
        if root:
           self.iterPreorderVisit(root, res)
        return res

    def recPreorderVisit(self, root, res): # recursive
        if root:
           res.append(root.val)
           self.preorderVisit(root.left, res)
           self.preorderVisit(root.right, res)
        return

    def iterPreorderVisit(self, root, res): # iterative
        stack = []
        while root or stack:
              if root:
                 res.append(root.val)
                 stack.append(root)
                 root = root.left
              else:
                 root = stack.pop()
                 root = root.right
        return res

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
    print ms.preorderTraversal(t1)


