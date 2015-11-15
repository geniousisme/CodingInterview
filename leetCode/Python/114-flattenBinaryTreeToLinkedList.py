# Time:  O(n)
# Space: O(h), h is height of binary tree
#
# Given a binary tree, flatten it to a linked list in-place.
#
# For example,
# Given
#
#          1
#         / \
#        2   5
#       / \   \
#      3   4   6
# The flattened tree should look like:
#    1
#     \
#      2
#       \
#        3
#         \
#          4
#           \
#            5
#             \
#              6
#

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# class LinkNode:
#       def __init__(self, data):
#           self.val  = data
#           self.next = None

class Solution1:
    def flatten(self, root):
        while root:
            if root.left:
                tmp = root.left
                while tmp.right:
                    tmp  = tmp.right
                tmp.right  = root.right
                root.right = root.left
                root.left  = None
            root = root.right

# draw a picture and you can understand the algo
class Solution(object):
    def flatten(self, root):
        while root:
            if root.left:
                tmp = root.left
                while tmp.right:
                    tmp = tmp.right
                tmp.right = root.right
                root.left = root.right
                root.left = None
            root = root.right


if __name__ == '__main__':
   s = Solution()
   test = TreeNode(1)
   test.left = TreeNode(2)
   test.left.left = TreeNode(3)
   test.left.right = TreeNode(4)
   test.right = TreeNode(5)
   test.right.right = TreeNode(6)
   s.flatten(test)
   # s.print_llst(s.flatten(test))






