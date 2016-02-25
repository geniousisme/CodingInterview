class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseI(self, head): # iterative
        start = None
        while head:
            nxt = head.next
            head.next = start
            start = head
            head = nxt
        return start

    def reverse(self, head): # recursive
        return self.reverse_helper(head, None)

    def reverse_helper(self, head, start):
        if head is None:
            return start
        else:
            nxt = head.next
            head.next = start
            return self.reverse_helper(nxt, head)

    def print_llst(self, head):
        llst = ""
        while head:
            llst += str(head.val)
            if head.next:
                llst += "->"
            head = head.next
        print llst

if __name__ == "__main__":
    s = Solution()
    l1 = ListNode(1)
    l2 = ListNode(2)
    l3 = ListNode(3)
    l4 = ListNode(4)
    l1.next = l2
    l2.next = l3
    l3.next = l4
    s.print_llst(s.reverse(l1))