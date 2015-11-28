# Give two nodes in a binary tree, find the distance between them:

# Thought: Dist(n1, n2) = Dist(root, n1) + Dist(root, n2) - 2*Dist(root, lca),
# lca is lowest common ancestor

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    '''
    Time:  O(n)
    Space: O(h)
    '''
    def distance(self, root, node1, node2):
        lca = self.find_lca(root, node1, node2)
        lca_dist   = self.root_node_dist(root, lca)
        node1_dist = self.root_node_dist(root, node1)
        node2_dist = self.root_node_dist(root, node2)
        return node1_dist + node2_dist - 2 * lca_dist

    def find_lca(self, root, node1, node2):
        if root is None:
            return None

        if root == node1 or root == node2:
            return root

        left_lca = self.find_lca(root.left, node1, node2)
        right_lca = self.find_lca(root.right, node1, node2)

        if left_lca and right_lca:
            return root

        return left_lca if left_lca is not None else right_lca

    def root_node_dist(self, root, node):
        if root is None:
            return -float("inf")
        if root == node:
            return 0
        return max(self.root_node_dist(root.left, node), self.root_node_dist(root.right, node)) + 1

if __name__ == "__main__":
    s = Solution()
    t1 = TreeNode(1)
    t2 = TreeNode(2)
    t3 = TreeNode(3)
    t4 = TreeNode(4)
    t5 = TreeNode(5)
    t6 = TreeNode(6)
    t7 = TreeNode(7)
    t8 = TreeNode(8)
    t1.left = t2
    t1.right = t3
    t2.left = t4
    t2.right = t5
    t3.left = t6
    t3.right = t7
    t6.right = t8
    print s.distance(t1, t4, t5)
    print s.distance(t1, t4, t6)
    print s.distance(t1, t3, t4)
    print s.distance(t1, t2, t4)
    print s.distance(t1, t8, t5)



