# Time:  O(n)
# Space: O(1)
#
# Given a binary tree, return the postorder traversal of its nodes' values.
#
# For example:
# Given binary tree {1,#,2,3},
#   1
#    \
#     2
#    /
#   3
# return [3,2,1].
#
# Note: Recursive solution is trivial, could you do it iteratively?
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
    def postorderTraversal(self, root):
        res = []
        self.iterPostOrder(root, res)
        return res

    def recurPostOrder(self, root, res):
        if root:
           self.recurPostOrder(root.left, res)
           self.recurPostOrder(root.right, res)
           res.append(root.val)
        return

    def iterPostOrder(self, root, res):
        stack = []
        prev = None
        if root:
           stack.append(root)
           while stack:
                 curr = stack[-1]
                 if (curr.left is None and curr.right is None) or (prev and (prev == curr.left or prev == curr.right)):
                    res.append(curr.val)
                    prev = stack.pop()
                 else:
                    if curr.right: stack.append(curr.right)
                    if curr.left:  stack.append(curr.left)
        return res

class Solution(object):
    def postorderTraversal(self, root):
        res = []; stack = []; last_traversed = None
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                parent = stack[-1]
                if parent.right in (None, last_traversed):
                    res.append(parent.val)
                    last_traversed = stack.pop()
                else:
                    root = parent.right
        return res

if __name__ == '__main__':
   s = Solution()
   test = TreeNode(1)
   test.left = TreeNode(2)
   test.right = TreeNode(3)
   test.left.left = TreeNode(4)
   test.left.right = TreeNode(5)
   test.right.left = TreeNode(6)
   test.right.right = TreeNode(7)
   print s.postorderTraversal(test)
