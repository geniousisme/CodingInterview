# Reverse a singly linked list.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseList(self, head):
        pass

class Solution(object):
    def reverseList(self, head):
        pass

class Solution2(object):
    def reverse_print_llst(self, head):
        if head is None:
            return
        self.reverse_print_llst(head.next)
        print head.val

if __name__ == "__main__":
    s2 = Solution2()
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(3)
    l1.next.next.next = ListNode(4)
    l1.next.next.next.next = ListNode(5)
    s2.reverse_print_llst(l1)


