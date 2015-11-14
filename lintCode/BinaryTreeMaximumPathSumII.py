# Medium Binary Tree Maximum Path Sum II

# Given a binary tree, find the maximum path sum from root.

# The path may end at any node in the tree.

# Have you met this question in a real interview? Yes
# Example
# Given the below binary tree:

#   1
#  / \
# 2   3
# return 4. (1->3)

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left  = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer}
    def __init__(self):
        self.max = -float('inf')

    def maxPathSum2(self, root):
        if not root:
            return 0
        self.path_sum_helper(root, 0)
        return self.max

    def path_sum_helper(self, root, curr_sum):
        if root.left is None and root.right is None:
            self.max = max(self.max, curr_sum + root.val)
            return
        if self.max < curr_sum + root.val:
            self.max = curr_sum + root.val
        if root.left:
            self.path_sum_helper(root.left, curr_sum + root.val)
        if root.right:
            self.path_sum_helper(root.right, curr_sum + root.val)

if __name__ == "__main__":
    s = Solution()
    t1 = TreeNode(1)
    t2 = TreeNode(2)
    t3 = TreeNode(1)
    t4 = TreeNode(-4)
    t5 = TreeNode(100)
    t1.left = t2
    t1.right = t3
    t3.left = t4
    t3.right = t5
    print s.maxPathSum2(t1)
