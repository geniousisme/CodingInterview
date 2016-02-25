# Time:  O(n)
# Space: O(h), h is height of binary tree
#
# Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.
#
# For example:
# Given the below binary tree and sum = 22,
#               5
#              / \
#             4   8
#            /   / \
#           11  13  4
#          /  \    / \
#         7    2  5   1
# return
# [
#    [5,4,11,2],
#    [5,8,4,5]
# ]


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution1:
    # @param {TreeNode} root
    # @param {integer} sum
    # @return {integer[][]}
    def __init__(self):
        self.res = []

    def pathSum(self, root, sum):
        if root:
           # print 'root'
           self.dfs(root, [], sum)
        return self.res

    def dfs(self, node, path, left_sum):
        if node:
           if node.right is None and node.left is None:
              if left_sum == node.val:
                 path.append(node.val)
                 self.res.append(list(path))
                 path.pop()
                 return
           path.append(node.val)
           self.dfs(node.right, path, left_sum - node.val)
           self.dfs(node.left,  path, left_sum - node.val)
           path.pop()
        return

class Solution(object):
    def __init__(self):
        self.res = []

    def pathSum(self, root, sum):
        if self.res:
            self.res = []
        if root:
            self.path_sum_helper(root, sum, [])
        return self.res

    def path_sum_helper(self, root, left_sum, curr_path):
        if root is None:
            return
        # need to make sure the root already reach the bottom of the tree
        if root.left is None and root.right is None and root.val == left_sum:
            self.res.append(curr_path + [root.val])
            return
        self.path_sum_helper(root.left, left_sum - root.val, curr_path + [root.val])
        self.path_sum_helper(root.right, left_sum - root.val, curr_path + [root.val])

if __name__ == '__main__':
   s = Solution()
   test = TreeNode(5)
   test.left = TreeNode(4)
   test.right = TreeNode(8)
   test.left.left = TreeNode(11)
   test.left.left.left = TreeNode(7)
   test.left.left.right = TreeNode(2)
   test.right.left = TreeNode(13)
   test.right.right = TreeNode(4)
   test.right.right.left = TreeNode(5)
   test.right.right.right = TreeNode(1)
   print s.pathSum(test, 22)

