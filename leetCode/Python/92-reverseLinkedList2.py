# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
def print_llst(head):
    llst = ""
    while head:
        llst += str(head.val)
        if head.next:
            llst += "->"
        head = head.next
    print llst

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        new_head = dummy # notice here, use new start node to prevent the starting from one case!

        for i in xrange(m - 1):
            dummy = dummy.next

        rstart = dummy.next # notice here, be careful the case of starting from 1!
        rend   = rstart
        start  = None

        for i in xrange(m, n + 1):
            nxt = rstart.next
            rstart.next = start
            start = rstart
            rstart = nxt

        dummy.next = start
        rend.next  = rstart

        return new_head.next

if __name__ == "__main__":
   s = Solution()
   l1 = ListNode(1)
   l2 = ListNode(2)
   l3 = ListNode(3)
   l4 = ListNode(4)
   l5 = ListNode(5)
   
   l1.next = l2
   l2.next = l3
   l3.next = l4
   l4.next = l5

   print_llst(s.reverseBetween(l1, 3, 5))
