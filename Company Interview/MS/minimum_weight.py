class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left  = None
        self.right = None

class Solution(object):
    def miniWeight(self, root):
        self.mini_weight = float("inf")
        self.mini_node   = None
        self.post_order_traverse(root)
        return self.mini_node

    def post_order_traverse(self, root):
        if root:
            self.post_order_traverse(root.left)
            self.post_order_traverse(root.right)
            curr_wieght = root.val
            if root.left:
                curr_wieght += root.left.val
            if root.right:
                curr_wieght += root.right.val
            if curr_wieght < self.mini_weight:
                self.mini_weight = curr_wieght
                self.mini_node   = root
        return

if __name__ == "__main__":
    s = Solution()
    t1 = TreeNode(5)
    t2 = TreeNode(-2)
    t3 = TreeNode(6)
    t4 = TreeNode(3)
    t5 = TreeNode(4)
    t1.left = t2
    t1.right = t3
    t2.left = t4
    t3.right = t5
    print s.miniWeight(t1).val

