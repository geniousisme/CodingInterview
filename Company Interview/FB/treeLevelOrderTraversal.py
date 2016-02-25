import collections

class Solution(object):
    def levelOrderTraversal(self, root):
        res = []; queue = collections.deque(); curr_lv = []; next_lv = []
        if root:
            queue.append(root)
            while queue:
                root = queue.popleft()
                curr_lv.append(root.val)
                if root.left:
                    next_lv.append(root.left)
                if root.right:
                    next_lv.append(root.right)
                if not queue:
                    queue.extend(next_lv)
                    res.append(curr_lv)
                    next_lv = []
                    curr_lv = []
        return res

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
    t1.right = t3
    t2.left = t4
    t2.right = t5
    t3.left = t6
    t3.right = t7
    print s.levelOrderTraversal(t1)