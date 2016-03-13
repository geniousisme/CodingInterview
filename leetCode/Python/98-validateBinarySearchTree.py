# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution: # recursive
    # @param {TreeNode} root
    # @return {boolean}
    # check the upper & lower blund method
    def isValidBST(self, root):
        inf = float('inf')
        return self.bstCheck(root, -inf, inf)

    def bstCheck(self, node, past_min, past_max):
        if node is None: return True
        if not past_min < node.val < past_max:
           return False
        return self.bstCheck(node.right, node.val, past_max) and \
               self.bstCheck(node.left, past_min, node.val)

class Solution(object): # iterative
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        stack = []
        prev = None; curr = None
        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            else:
                curr = stack.pop()
                if prev and curr.val <= prev.val:
                    return False
                else:
                    prev = curr
                root = curr.right
        return True