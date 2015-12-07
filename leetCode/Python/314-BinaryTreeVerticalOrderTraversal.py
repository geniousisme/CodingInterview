# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

import collections
class Solution(object):
    def verticalOrder(self, root):
        """
        Time:  O(n)
        Space: O(n)
        """
        if not root:
            return []
        lookup = collections.defaultdict(list)
        queue = collections.deque()
        queue.append((root, 0))
        max_idx = min_idx = 0
        while queue:
            root, idx = queue.popleft()
            lookup[idx].append(root.val)
            if root.left:
                min_idx = min(min_idx, idx - 1)
                queue.append((root.left,  idx - 1))
            if root.right:
                max_idx = max(max_idx, idx + 1)
                queue.append((root.right, idx + 1))
        return [lookup[i] for i in xrange(min_idx, max_idx + 1)]

if __name__ == "__main__":
    s = Solution()
    t3 = TreeNode(3)
    t9 = TreeNode(9)
    t20 = TreeNode(20)
    t4 = TreeNode(4)
    t5 = TreeNode(5)
    t2 = TreeNode(2)
    t7 = TreeNode(7)
    t3.left = t9
    t3.right = t20
    t9.left = t4
    t9.right = t5
    t20.left = t2
    t20.right = t7
    print s.verticalOrder(t3)




