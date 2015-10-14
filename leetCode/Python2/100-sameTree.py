class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSameTreeRec(self, p, q): # recursive
        if p is None and q is None:
            return True
        if p and q and p.val == q.val:
            return self.isSameTree(p.left, q.left) and                         \
                   self.isSameTree(p.right, q.right)
        return False

    def isSameTree(self, p, q): # iterative
        stack = []
        stack.append([p, q])
        while stack:
            p, q = stack.pop()
            if p is not None and q is None:
                return False
            elif p is None and q is not None:
                return False
            elif p and q and p.val != q.val:
                return False
            else:
                if p is None and q is None:
                    continue
                stack.append([p.left, q.left])
                stack.append([p.right, q.right])
        return True

if __name__ == "__main__":
    s = Solution()
    t1 = TreeNode(1)
    t1.left = TreeNode(2)
    t1.right = TreeNode(3)
    t2 = TreeNode(1)
    t2.left = TreeNode(2)
    t2.right = TreeNode(3)
    print s.isSameTree(t1, t2)