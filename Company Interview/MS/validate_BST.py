class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left  = None
        self.right = None

class Solution(object):
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