# Time:  O(n)
# Space: O(h), h is height of binary tree
#
# Given a binary tree, determine if it is height-balanced.
#
# For this problem, a height-balanced binary tree is defined as a binary tree 
# in which the depth of the two subtrees of every node never differ by more than 1.
#

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    # @param root, a tree node
    # @return a boolean
    def isBalanced(self, root):
        return (self.getHeight(root) >= 0)

    def getHeight(self, root):
        if root is None:
            return 0
        left_height, right_height = self.getHeight(root.left), self.getHeight(root.right)
        # use the height to check if it is a balanced binary tree or not
        # if not, return -1, make it less than or equal to zero
        if left_height < 0 or right_height < 0 or abs(left_height - right_height) > 1:
            return -1
        return max(left_height, right_height) + 1

class Solution1:
    def height(self, root):
        if root is None:
           return 0
        else:
           return max(self.height(root.right), self.height(root.left)) + 1

    def isBalanced(self, root):
        if root is None: return True
        if abs(self.height(root.right) - self.height(root.left)) > 1:
           return False
        else:
           return self.isBalanced(root.right) and self.isBalanced(root.left)



if __name__ == '__main__':
   s = Solution()
   test = TreeNode(1)
   # test.left = TreeNode(0)
   # test.left.left = TreeNode(0)
   test.right = TreeNode(2)
   test.right.right = TreeNode(3)
   print s.isBalanced(test)

