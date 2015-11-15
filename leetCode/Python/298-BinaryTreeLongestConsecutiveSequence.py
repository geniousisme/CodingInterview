# Given a binary tree, find the length of the longest consecutive sequence path.

# The path refers to any sequence of nodes from some starting node
# to any node in the tree along the parent-child connections.
# The longest consecutive path need to be from parent to child (cannot be the reverse).

# For example,

#    1
#     \
#      3
#     / \
#    2   4
#         \
#          5
# Longest consecutive sequence path is 3-4-5, so return 3.

#    2
#     \
#      3
#     /
#    2
#   /
#  1
# Longest consecutive sequence path is 2-3,not3-2-1, so return 2.

# Time:  O(n)
# Space: O(h)
class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution(object):
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.longest_consecutive_helper(root, None, 0)

    def longest_consecutive_helper(self, curr, parent, max_len):
        if curr is None:
            return max_len
        max_len = max_len + 1 if parent and curr.val == parent.val + 1 else 1
        return max(self.longest_consecutive_helper(curr.left,  curr, max_len), \
                   self.longest_consecutive_helper(curr.right, curr, max_len))

if __name__ == "__main__":
    s = Solution()
    t1 = TreeNode(2)
    t2 = TreeNode(3)
    t3 = TreeNode(4)
    t4 = TreeNode(1)
    t1.right = t2
    t2.left = t3
    t3.left = t4
    print s.longestConsecutive(t1)


