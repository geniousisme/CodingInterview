# Time:  O(n)
# Space: O(1)
#
# Given a sorted linked list, delete all nodes that have duplicate numbers,
#  leaving only distinct numbers from the original list.
#
# For example,
# Given 1->2->3->3->4->4->5, return 1->2->5.
# Given 1->1->1->2->3, return 2->3.
# Definition for singly-linked list.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def deleteDuplicates(self, head):
        if head is None or head.next is None: return head
        start = ListNode(-99); start.next = head
        prev = start
        post = start.next
        while prev.next:
              # if post.next.val == prev.next.val, which means there are reapted value
              # you should iterate the ptr to find the different one.
              while post.next and prev.next.val == post.next.val:
                    post = post.next
              # now we find the different one

              # for this case, which mean the valure is different at first time
              # then we just need to move both ptr forward to keep checking
              if post == prev.next:
                 prev = prev.next
                 post = prev.next
              else:
              # for this case, which means that we need to delete the repeated value nodes
              # then we make prev.next equal to post.next directly.
                 prev.next = post.next
        return start.next

    def print_llst(self, head):
        llst = ""
        while head:
              llst += str(head.val)
              if head.next:
                 llst += '->'
              head = head.next
        print llst

if __name__ == '__main__':
   s = Solution()
   test = ListNode(1)
   test.next = ListNode(1)
   test.next.next = ListNode(1)
   test.next.next.next = ListNode(2)
   test.next.next.next.next = ListNode(2)
   test.next.next.next.next.next = ListNode(4)
   test.next.next.next.next.next.next = ListNode(4)
   # s.deleteDuplicates(test)
   s.print_llst(s.deleteDuplicates(test))