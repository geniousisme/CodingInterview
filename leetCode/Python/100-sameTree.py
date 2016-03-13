# Given two binary trees, write a function to check if they are equal or not.

# Two binary trees are considered equal if they are structurally identical 
# and the nodes have the same value.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

'''
Time:  O(n)
Space: O(n)
'''

class Solution1(object):
    def isSameTree(self, p, q): # recursive
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p is None and q is None:
            return True
        if p and q and p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        return False

'''
Time:  O(n)
Space: O(n)
'''
class Solution(object):
    def isSameTree(self, p, q): # iterative
        queue = []
        queue.append((p, q))
        while queue:
            p, q = queue.pop()
            if p is None and q is None:
                continue
            elif p and q and p.val == q.val:
                queue.append((p.left, q.left))
                queue.append((p.right, q.right))
            else:
                return False
        return True



