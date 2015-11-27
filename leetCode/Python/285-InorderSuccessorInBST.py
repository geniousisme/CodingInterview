# Given a binary search tree and a node in it,
# find the in-order successor of that node in the BST.
# Note: If the given node has no in-order successor in the tree, return null.

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode

        Time:  O(h)
        Space: O(1)
        """
        # if there is a right subtree for p
        # then we only need to find the most left subtree of p
        if p.right:
            p = p.right
            while p.left:
                p = p.left
            return p
        else:
            # very smart way for this part,
            # if we get the following tree:

            #      9
            #    /   \
            #   5    15
            #  / \   / \
            # 1   7 10 20

            # when root val > p val, then we store it first as successor candidate
            # then go to left tree for closer(smaller) values
            # when root val < p val, then we go to right tree but not store anything,
            # since we need to find the one larger than p val.
            successor = None
            while root and root != p:
                if root.val > p.val:
                    successor = root
                    root = root.left
                else:
                    root = root.right
            return successor

if __name__ == "__main__":
    s = Solution()
    t9 = TreeNode(9)
    t5 = TreeNode(5)
    t15 = TreeNode(15)
    t1 = TreeNode(1)
    t7 = TreeNode(7)
    t10 = TreeNode(10)
    t20 = TreeNode(20)

    t9.left = t5
    t9.right = t15
    t5.left = t1
    t5.right = t7
    t15.left = t10
    t15.right = t20

    print s.inorderSuccessor(t9, t20)
    print s.inorderSuccessor(t9, t7).val
    print s.inorderSuccessor(t9, t5).val
    print s.inorderSuccessor(t9, t10).val










