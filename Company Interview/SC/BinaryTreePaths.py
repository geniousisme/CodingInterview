# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):
        if not root:
            return []
        self.paths = []
        self.binary_tree_path_finder(str(root.val), root)
        return self.paths

    def binary_tree_path_finder(self, path, root):
        if root.left is None and root.right is None:
            self.paths.append(path)
            return
        if root.left:
            self.binary_tree_path_finder(path + str(path.left.val), root.left)
        if root.right:
            self.binary_tree_path_finder(path + str(path.right.val), root.right)
