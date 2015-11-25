# Given a non-empty binary search tree and a target value,
# find the value in the BST that is closest to the target.

# Note: Given target value is a floating point.
# You are guaranteed to have only one unique value in the BST that is closest to the target.

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left  = None
        self.right = None


class Solution(object): # recursive
    '''
    Time:  O(n)
    Space: O(h)
    '''
    def __init__(self):
        self.closest = float("inf")
        self.target = 0

    def closestValue(self, root, target):
        self.target = target
        if root:
            self.closest_val_helper(root)
        return self.closest

    def closest_val_helper(self, root):
        if root:
            if abs(root.val - self.target) < abs(self.closest - self.target):
                self.closest = root.val
            if root.val > self.target:
                self.closest_val_helper(root.left)
            else:
                self.closest_val_helper(root.right)
        return

class Solution(object): # iterative
    '''
    Time:  O(n)
    Space: O(1)
    '''
    def closestValue(self, root, target):
        gap = float("inf")
        closest = None
        while root:
            if gap > abs(root.val - target):
                gap = abs(root.val - target)
                closest = root
            if target == root.val:
                break
            if target > root.val:
                root = root.right
            else:
                root = root.left
        return closest.val

if __name__ == "__main__":
    s = Solution()
    t13 = TreeNode(13)
    t5 = TreeNode(5)
    t1 = TreeNode(1)
    t9 = TreeNode(9)
    t19 = TreeNode(19)
    t21 = TreeNode(21)
    t37 = TreeNode(37)
    t13.left = t5
    t13.right = t21
    t5.left = t1
    t5.right = t9
    t21.left = t19
    t21.right = t37

    print s.closestValue(t13, 0)
    print s.closestValue(t13, 4)
    print s.closestValue(t13, 12)
    print s.closestValue(t13, 18)
    print s.closestValue(t13, 23)
    print s.closestValue(t13, 40)
    print s.closestValue(t13, 100)









