# Time:  O(n)
# Space: O(1)
#
# Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.
#
# You should preserve the original relative order of the nodes in each of the two partitions.
#
# For example,
# Given 1->4->3->2->5->2 and x = 3,
# return 1->2->2->4->3->5.
#

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} x
    # @return {ListNode}
    def partition(self, head, x):
        if head is None or head.next is None: return head
        small_start = ListNode(-1); large_start = ListNode(-1)
        small_start.next = large_start.next = head
        stmp = small_start; ltmp = large_start
        while stmp.next:
              if stmp.next.val < x:
                 stmp = stmp.next
                 ltmp.next = ltmp.next.next
              else:
                 ltmp = ltmp.next
                 stmp.next = stmp.next.next
        stmp.next = large_start.next
        return small_start.next

    def partition2(self, head, x):
        head1 = ListNode(0)
        head2 = ListNode(0)
        Tmp = head
        phead1 = head1
        phead2 = head2
        while Tmp:
            if Tmp.val < x:
                phead1.next = Tmp
                Tmp = Tmp.next
                phead1 = phead1.next
                phead1.next = None
            else:
                phead2.next = Tmp
                Tmp = Tmp.next
                phead2 = phead2.next
                phead2.next = None
        phead1.next = head2.next
        head = head1.next
        return head


def print_llst(head):
    llst = ''
    while head:
          llst += str(head.val)
          if head.next:
             llst += '->'
          head = head.next
    print llst

if __name__ == '__main__':
   s = Solution()
   test = ListNode(1)
   test.next = ListNode(4)
   test.next.next = ListNode(3)
   test.next.next.next = ListNode(2)
   test.next.next.next.next = ListNode(5)
   test.next.next.next.next.next = ListNode(2)
   print_llst(s.partition(test, 3))

