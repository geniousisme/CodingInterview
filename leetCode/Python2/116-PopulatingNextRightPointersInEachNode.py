class TreeLinkNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution(object):
    def __init__(self):
        self.level = []
    def connectI(self, root):
        """
        :type root: TreeLinkNode
        :rtype: nothing
        """
        self.connect_helper(root, 1)
        return

    def connect_helper(self, root, depth): # dfs
        if root:
            if len(self.level) < depth:
                self.level.append(root)
            else:
                self.level[depth - 1].next = root
                self.level[depth - 1] = self.level[depth - 1].next
            self.connect_helper(root.left,  depth + 1)
            self.connect_helper(root.right, depth + 1)
        return

    def connectII(self, root): # bfs
        queue = [root]
        next_lv = []
        node = None
        while queue:
            root = queue.pop(0)
            if root:
                if node is None:
                    node = root
                else:
                    node.next = root
                    node = node.next
                next_lv.extend([root.left, root.right])
            if not queue:
                queue.extend(next_lv)
                next_lv = []
                node = None
        return

    def connect(self, root):
        if root:
            if root.left:
                root.left.next = root.right
            if root.right and root.next:
                root.right.next = root.next.left
            self.connect(root.left)
            self.connect(root.right)
        return

if __name__ == "__main__":
    s = Solution()
    t1 = TreeLinkNode(1)
    t2 = TreeLinkNode(2)
    t3 = TreeLinkNode(3)
    t1.left = t2
    t1.right = t3
    s.connect(t1)






