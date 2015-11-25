# Given a binary tree and a sum, determine if the tree has a root-to-leaf path
# such that adding up all the values along the path equals the given sum.
#
# For example:
# Given the below binary tree and sum = 22,
#               5
#              / \
#             4   8
#            /   / \
#           11  13  4
#          /  \      \
#         7    2      1
# return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
#

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    '''
    Time:  O(n)
    Space: O(h)
    '''
    def hasPathSum(self, root, sum):
        if root is None:
           return False
        return self.pathSumCheck(root, 0, sum)

    def pathSumCheck(self, node, curr_sum, goal_sum):
        if node is None:
           return False
        curr_sum += node.val
        if node.right is None and node.left is None:
           return curr_sum == goal_sum
        else:
           return self.pathSumCheck(node.right, curr_sum, goal_sum) or \
                  self.pathSumCheck(node.left,  curr_sum, goal_sum)


if __name__ == '__main__':
   s = Solution()
   test = TreeNode(1)
   test.right = TreeNode(2)
   print s.hasPathSum(test, 2)
   print s.hasPathSum(test, 1)

