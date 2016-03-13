
# Time:  O(n)
# Space: O(h), h is height of binary tree
#
# Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.
# 
# An example is the root-to-leaf path 1->2->3 which represents the number 123.
# 
# Find the total sum of all root-to-leaf numbers.
# 
# For example,
# 
#     1
#    / \
#   2   3
# The root-to-leaf path 1->2 represents the number 12.
# The root-to-leaf path 1->3 represents the number 13.
# 
# Return the sum = 12 + 13 = 25.
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution1:
    # @param {TreeNode} root
    # @return {integer}
    def __init__(self):
        self.res = []

    def sumNumbers(self, root):
        res = []
        self.dfs(root, "", res)
        # print res
        return sum(res)

    def dfs(self, root, num, res):
        if root:
           if root.right is None and root.left is None:
              res.append(int(num + str(root.val)))
              return
           self.dfs(root.left,  num + str(root.val), res)
           self.dfs(root.right, num + str(root.val), res)
        return

class Solution(object):
    def sumNumbers(self, root):
        if not root:
            return 0
        return self.sum_num_helper(root, 0)

    def sum_num_helper(self, root, curr_num):
        if root is None:
            return 0

        if root.left is None and root.right is None:
            return curr_num * 10 + root.val

        return self.sum_num_helper(root.left, curr_num * 10 + root.val) + self.sum_num_helper(root.right, curr_num * 10 + root.val)


if __name__ == '__main__':
   s = Solution()
   test = TreeNode(1)
   test.left = TreeNode(2)
   test.right = TreeNode(3)
   test.left.left = TreeNode(4)
   test.left.right = TreeNode(5)
   test.right.left = TreeNode(6)
   test.right.right = TreeNode(7)
   print s.sumNumbers(test)
   print s.sumNumbers(None)



