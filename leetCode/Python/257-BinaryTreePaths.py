# Time:  O(n * h)
# Space: O(h)
#
# Given a binary tree, return all root-to-leaf paths.
#
# For example, given the following binary tree:
#
#   1
#  /   \
# 2     3
#  \
#   5
# All root-to-leaf paths are:
#
# ["1->2->5", "1->3"]
#
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution1:
    # @param {TreeNode} root
    # @return {string[]}
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
    def binaryTreePaths(self, root):
        if root is None:
            return []
        queue = [ [root, str(root.val)] ]
        ans = []
        while queue:
            front, path = queue.pop(0)
            if front.left is None and front.right is None:
                ans += path,
                continue
            if front.left:
                queue += [front.left, path + "->" + str(front.left.val)],
            if front.right:
                queue += [front.right, path + "->" + str(front.right.val)],
        return ans

if __name__ == "__main__":
   s = Solution()
   test = TreeNode(1)
   test.left = TreeNode(2)
   test.right = TreeNode(3)
   test.left.left = TreeNode(4)
   test.left.right = TreeNode(5)
   test.right.right = TreeNode(6)
   print s.binaryTreePaths(test)




        