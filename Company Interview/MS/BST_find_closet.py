class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left  = None
        self.right = None

class Solution(object):
    def closest_value(self, root, target):
        min_diff   = float("inf")
        closet_val = None
        self.closest_value_helper(root, min_diff, closet_val, target)
        return closet_val

    def closet_val_helper(self, root, min_diff, closet_val, target):
        if root:
            if root.val < target and target - root.val < min_diff:
                min_diff   = target - root.val
                closet_val = root.val
            if min_diff == 0:
                return
            elif root.val > target:
                self.closet_val_helper(root.left, min_diff, closet_val, target)
            elif root.val < target:
                self.closet_val_helper(root.right, min_diff, closet_val, target)
        return

