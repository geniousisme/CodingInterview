# Time:  O(n)
# Space: O(h), h is height of binary tree
#
# Given a binary tree, find the maximum path sum.
# 
# The path may start and end at any node in the tree.
# 
# For example:
# Given the below binary tree,
# 
#        1
#       / \
#      2   3
# Return 6.
#
# Definition for a  binary tree node


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.max_sum = float("-inf")
        self.max_path_sum_helper(root)
        return self.max_sum

    def max_path_sum_helper(self, root):
        if not root:
            return 0
        left_sum = max(0, self.max_path_sum_helper(root.left))
        right_sum = max(0, self.max_path_sum_helper(root.right))
        self.max_sum = max(self.max_sum, root.val + left_sum + right_sum)
        return root.val + max(left_sum, right_sum)


        