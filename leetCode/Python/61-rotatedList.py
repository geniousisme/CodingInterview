# Time:  O(n)
# Space: O(1)
#
# Given a list, rotate the list to the right by k places, where k is non-negative.
#
# For example:
# Given 1->2->3->4->5->NULL and k = 2,
# return 4->5->1->2->3->NULL.
#


# # Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:

    def rotateRight(self, head, k):
        if not k: return head
        if head is None: return head
        start = ListNode(-1); start.next = head; new_end = start
        length = 0
        tmp = start
        while tmp.next:
              length += 1
              tmp = tmp.next
        step = length - (k % length)
        tmp.next = start.next # connect the end to the head

        new_start = head
        for i in xrange(step):
            new_start = new_start.next # get the new start node
            new_end   = new_end.next # get the new end node
        new_end.next = None # set new end of the llst

        return new_start

    def print_llst(self, head):
        llst = ""
        while head:
              llst += str(head.val)
              if head.next:
                 llst += "->"
              head = head.next
        print llst

if __name__ == '__main__':
  s = Solution()
  test = ListNode(1)
  test.next = ListNode(2)
  # test.next.next = ListNode(3)
  # test.next.next.next = ListNode(4)
  # test.next.next.next.next = ListNode(5)
  s.print_llst(test)
  s.print_llst(s.rotateRight(test, 9))
# s.print_llist(s.rotateRight(test, 5))
