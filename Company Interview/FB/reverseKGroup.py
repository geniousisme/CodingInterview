class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverse(self, start, end):
        new_head = ListNode(0)
        new_head.next = start
        while new_head.next != end:
            nxt = start.next
            start.next = nxt.next
            nxt.next = start
            new_head.next = nxt
        print_llst(start)
        return end, start

    def reverseKGroup(self, head, k):
        if head is None:
            return head
        new_head = ListNode(-1); new_head.next = head
        start = new_head
        while start.next:
            end = start
            for i in xrange(k - 1):
                end = end.next
                if end.next is None:
                    return new_head.next
            start.next, start = self.reverse(start.next, end.next)
        return new_head.next


def print_llst(head):
    llst = ""
    while head:
        llst += str(head.val)
        if head.next:
            llst += "->"
        head = head.next
    print llst

if __name__ == "__main__":
    s = Solution()
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    print_llst(s.reverseKGroup(head, 2))



