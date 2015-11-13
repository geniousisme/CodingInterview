# Time:  O(n ^ 2)
# Space: O(1)
#
# Sort a linked list using insertion sort.
#


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}

    def insertionSortList(self, head):
        if head is None or self.is_sorted(head):
            return head
        dummy = ListNode(float("-inf"))
        dummy.next = head
        curr = dummy
        while curr.next:
            if curr.val > curr.next.val:
                prev = dummy
                while prev.next.val < curr.next.val:
                    prev = prev.next
                tmp = curr.next
                curr.next = tmp.next
                tmp.next = prev.next
                prev.next = tmp
            else:
                curr = curr.next
        return dummy.next

    def is_sorted(self, head):
        while head.next:
            if head.val > head.next.val:
                return False
            head = head.next
        return True

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
   test.next = ListNode(4)
   test.next.next = ListNode(0)
   test.next.next.next = ListNode(3)
   test.next.next.next.next = ListNode(2)
   test.next.next.next.next.next = ListNode(5)

   s.print_llst(s.insertionSortList(test))

