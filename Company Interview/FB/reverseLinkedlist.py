# Reverse a singly linked list.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseList(self, head):
        start = None
        end = head
        while head:
            nxt = head.next
            head.next = start
            start = head
            head = nxt
        return start

class Solution1(object):
    def reverseList(self, head):
        pass

class Solution2(object):
    def reverse_print_llst(self, head):
        if head is None:
            return
        self.reverse_print_llst(head.next)
        print head.val

def print_llst(head):
    llst = ""
    while head:
        llst += str(head.val)
        if head.next:
            llst += "->"
        head = head.next
    print llst

if __name__ == "__main__":
    s2 = Solution2()
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(3)
    l1.next.next.next = ListNode(4)
    l1.next.next.next.next = ListNode(5)
    s2.reverse_print_llst(l1)
    s = Solution()
    print_llst(s.reverseList(l1))


