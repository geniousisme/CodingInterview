class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def biggestKthValues(self, root):
        res = []; stack = []
        while root or stack:
            if root:
                stack.append(root)
                root = root.right
            else:
                top = stack.pop()
                res.append(top.val)
                root = top.left
        return res

if __name__ == "__main__":
    s = Solution()
    t9 = TreeNode(9)
    t1 = TreeNode(1)
    t5 = TreeNode(5)
    t7 = TreeNode(7)
    t13 = TreeNode(13)
    t11 = TreeNode(11)
    t15 = TreeNode(15)
    t9.left = t5
    t9.right = t13
    t5.left = t1
    t5.right = t7
    t13.left = t11
    t13.right = t15
    print s.biggestKthValues(t9)



