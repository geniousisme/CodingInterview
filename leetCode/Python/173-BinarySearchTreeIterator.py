# Time:  O(1)
# Space: O(h), h is height of binary tree
#
# Implement an iterator over a binary search tree (BST).
# Your iterator will be initialized with the root node of a BST.
#
# Calling next() will return the next smallest number in the BST.
#
# Note: next() and hasNext() should run in average O(1) time
# and uses O(h) memory, where h is the height of the tree.
#

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = []
        self.push_left(root)


    def hasNext(self):
        """
        :rtype: bool
        """
        return bool(self.stack)

    def next(self):
        """
        :rtype: int
        """
        smallest = self.stack.pop()
        self.push_left(smallest.right)
        return smallest.val

    def push_left(self, root):
        while root:
            self.stack.append(root)
            root = root.left


# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())