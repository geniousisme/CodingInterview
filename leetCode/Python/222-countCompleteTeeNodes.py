# Time:  O(h * logn) = O((logn)^2)
# Space: O(1)

# Given a complete binary tree, count the number of nodes.
#
# In a complete binary tree every level, except possibly the last,
# is completely filled, and all nodes in the last level are as far
# left as possible. It can have between 1 and 2h nodes inclusive at
# the last level h.

# Definition for a binary tree node.
# Chris:Still dont know whats wrong for cant be accepted.
# maybe checkout later.

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution1(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        right_height = left_height = 0
        ltree, rtree = root, root
        while ltree:
            left_height  += 1
            ltree  = ltree.left
        while rtree:
            right_height += 1
            rtree = rtree.right
        if right_height == left_height:
            return 2 ** left_height - 1
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)

class Solution2:
    # @param {TreeNode} root
    # @return {integer}
    def __init__(self):
        self.count = 0
    
    def countNodes(self, root):
        if root:
           left_depth  = self.countDepth(root, 'left')
           right_depth = self.countDepth(root, 'right')
           if left_depth == right_depth:
              return 2 ** left_depth - 1
           else:
              self.countRecursive(root)
        return self.count

    def countDepth(self, root, direction):
        if root is None:
           return 0
        if direction == 'left':
           next = root.left
        else: # 'right'
           next = root.right
        return 1 + self.countDepth(next, direction)
    
    def countRecursive(self, root):
        if root is None:
           return
        self.count += 1
        self.countRecursive(root.right)
        self.countRecursive(root.left)

    def countRecursive2(self, root):
        if root is None:
           return 0
        return self.countRecursive2(root.right) + self.countRecursive2(root.left) + 1

class Solution:
    # @param {TreeNode} root
    # @return {integer}
    def countNodes(self, root):
        if root is None:
            return 0
        
        node, level = root, 0
        while node.left is not None:
            node = node.left
            level += 1
        
        # Binary search.
        left, right = 2 ** level, 2 ** (level + 1)
        while left < right:
            mid = left + (right - left) / 2
            if not self.exist(root, mid):
                right = mid
            else:
                left = mid + 1
                
        return left - 1
    
    # Check if the nth node exist.
    def exist(self, root, n):
        k = 1
        while k <= n:
            k <<= 1
        k >>= 2
        
        node = root
        while k > 0:
            if (n & k) == 0:
                node = node.left
            else:
                node = node.right
            k >>= 1
        return node is not None


if __name__ == '__main__':
   s = Solution()
   
   test = TreeNode(4)
   test.right = TreeNode(7)
   test.left  = TreeNode(2)
   test.right.right = TreeNode(9)
   test.right.left = TreeNode(6)
   test.left.right = TreeNode(3)
   test.left.left = TreeNode(1)

   # print s.countDepth(test, 'right')
   # print s.countDepth(test, 'left')
   # print s.countNodes(test)
   print s.countRecursive2(test)

