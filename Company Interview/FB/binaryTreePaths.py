# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution1:
    # @param {TreeNode} root
    # @return {string[]}
    '''
    Time:  O(n * h)
    Space: O(h)
    '''
    def __init__(self):
        self.res = []

    def binaryTreePaths(self, root):
        if root:
           self.traverse(root, str(root.val))
        return self.res

    def traverse(self, node, path):
        if node.right is None and node.left is None:
           self.res.append(path)
           return
        if node.left:
           self.traverse(node.left, path + '->' + str(node.left.val))
        if node.right:
           self.traverse(node.right, path + '->' + str(node.right.val))


class Solution(object):
    # @param {TreeNode} root
    # @return {string[]}
    '''
    Time:  O(n * h)
    Space: O(h)
    '''
    def binaryTreePaths(self, root):
        res = []
        if root:
            stack = [(root, str(root.val))]
            while stack:
                root, path = stack.pop()
                if root.left is None and root.right is None:
                    res.append(path)
                if root.left:
                    stack.append((root.left, path + "->" + str(root.left.val)))
                if root.right:
                    stack.append((root.right, path + "->" + str(root.right.val)))
        return res

if __name__ == "__main__":
   s = Solution()
   test = TreeNode(1)
   test.left = TreeNode(2)
   test.right = TreeNode(3)
   test.left.left = TreeNode(4)
   test.left.right = TreeNode(5)
   test.right.right = TreeNode(6)
   print s.binaryTreePaths(test)