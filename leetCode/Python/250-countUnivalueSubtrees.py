# Given a binary tree, count the number of uni-value subtrees.
# A Uni-value subtree means all nodes of the subtree have the same value.

# For example:
# Given binary tree,

#               5
#              / \
#             1   5
#            / \   \
#           5   5   5

# return 4.

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left  = None
        self.right = None

class Solution(object):
    '''
    Time:  O(n)
    Space: O(h)
    '''
    def __init__(self):
        self.count = 0

    def countUnivalSubtrees(self, root):
        self.is_univalue(root)
        return self.count

    def is_univalue(self, root):
        # if we meet the end of the root
        if root is None:
            return True

        # this is for the uni value case
        if root.right is None and root.left is None:
            self.count += 1
            return True

        is_left_unival  = self.is_univalue(root.left)
        is_right_unival = self.is_univalue(root.right)

        if is_left_unival and is_right_unival                                  \
            and (root.right is None or root.val == root.right.val)             \
            and (root.left  is None or root.val == root.left.val):
            self.count += 1
            return True

        return False

if __name__ == "__main__":
    s = Solution()
    root = TreeNode(5)
    root.left = TreeNode(1)
    root.right = TreeNode(5)
    root.left.left = TreeNode(5)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(5)
    print s.countUnivalSubtrees(root)