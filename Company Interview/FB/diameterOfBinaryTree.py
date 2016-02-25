class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def diameter(self, root):
        # lheight = rheight = 0
        # ldiameter = rdiameter = 0
        if not root:
            return 0, 0

        ldiameter, lheight = self.diameter(root.left)
        rdiameter, rheight = self.diameter(root.right)

        height = max(lheight, rheight) + 1
        return max(lheight + rheight + 1, ldiameter, rdiameter), height

if __name__ == "__main__":
    s = Solution()
    t1 = TreeNode(1)
    t2 = TreeNode(2)
    t3 = TreeNode(3)
    t4 = TreeNode(4)
    t5 = TreeNode(5)
    t6 = TreeNode(6)
    t7 = TreeNode(7)
    t1.left = t2
    t2.right = t4
    t2.left = t3
    t3.left = t7
    t4.right = t5
    t5.right = t6
    print s.diameter(t1)