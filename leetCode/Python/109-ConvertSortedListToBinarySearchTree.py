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
    # @param head, a list node
    # @return a tree node
    def sortedListToBST(self, head):
        length = 0
        curr = head
        # count the total length of the linked list
        while curr:
            length += 1
            curr = curr.next
        # make it easier to manipulate
        self.head = head
        return self.convert_sorted_list_bst_helper(0, length)

    def convert_sorted_list_bst_helper(self, start, end):
        # if we already reach the end of the linked list, return None
        if start == end:
            return None
        # find the mid(root for BST) first
        mid = start + (end - start) / 2
        # find the left child of the root.
        left = self.convert_sorted_list_bst_helper(start, mid)
        # assign the node for the root
        root = TreeNode(self.head.val)
        # connect left to the root
        root.left = left
        # move it to the next head
        self.head = self.head.next
        # connect right to the head
        root.right = self.convert_sorted_list_bst_helper(mid + 1, end)
        return root



