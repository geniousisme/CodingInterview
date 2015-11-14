# Time:  O(n)
# Space: O(logn)
#
# Given a singly linked list where elements are sorted in ascending order, 
# convert it to a height balanced BST.
#
# Definition for a  binary tree node

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution1:
    # @param {ListNode} head
    # @return {TreeNode}
    def sortedListToBST(self, head):
        sorted_list = []; length = 0
        while head:
              sorted_list.append(head.val)
              head = head.next
              length += 1
        return self.buildBST(sorted_list, 0, length - 1)

    def buildBST(self, lst, start, end):
        if start > end: return None
        mid = (start + end) / 2
        root = TreeNode(lst[mid])
        root.right = self.buildBST(lst, mid + 1, end)
        root.left  = self.buildBST(lst, start, mid - 1)
        return root

class Solution(object):
    head = None
    # @param head, a list node
    # @return a tree node
    def sortedListToBST(self, head):
        current, length = head, 0
        while current is not None:
            current, length = current.next, length + 1
        self.head = head
        return self.sortedListToBSTRecu(0, length)

    def sortedListToBSTRecu(self, start, end):
        if start == end:
            return None
        mid = start + (end - start) / 2
        left = self.sortedListToBSTRecu(start, mid)
        current = TreeNode(self.head.val)
        current.left = left
        self.head = self.head.next
        current.right = self.sortedListToBSTRecu(mid + 1, end)
        return current