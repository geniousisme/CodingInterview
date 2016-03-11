class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
        self.down = None

class Solution(object):
    def flattenLinkedList(self, head):
        dummy = ListNode(-1); dummy.next = head
        pre = dummy; curr = head
        while pre.next:
            if pre.next.down:
                nxt = curr.next
                new_head = pre.next.down
                new_dummy = new_head
                while new_dummy.next:
                    new_dummy = new_dummy.next
                pre.next = new_head
                new_dummy.next = curr
                pre = curr
                curr = curr.next
            else:
                pre = pre.next
                curr = curr.next
        return dummy.next

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
    l1 = ListNode(1)
    l2 = ListNode(2)
    l3 = ListNode(3)
    l4 = ListNode(4)
    l5 = ListNode(5)
    l6 = ListNode(6)
    l7 = ListNode(7)
    l1.next = l2
    l1.down = ListNode(-3)
    l1.down.next = ListNode(-4)
    l1.down.next.next = ListNode(-5)
    l2.next = l3
    l2.down = ListNode(0)
    l2.down.next = ListNode(-1)
    l2.down.next.next = ListNode(-2)
    l3.next = l7
    l7.down = l4
    l4.next = l5
    l5.next = l6
    print_llst(s.flattenLinkedList(l1))




