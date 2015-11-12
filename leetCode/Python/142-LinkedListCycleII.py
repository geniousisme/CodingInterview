# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a list node
    def detectCycle(self, head):
        # no cycle or only get one node or no node
        if head is None or head.next is None:
            return None

        slow = head
        fast = head
        
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
    
        if fast is None or fast.next is None:
            return None

        slow = head

        while slow and fast and fast.next:
            if slow == fast:
                return slow
            slow = slow.next
            fast = fast.next # notice here, just move as fast as slow!!

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution2:
    # @param head, a ListNode
    # @return a list node
    def detectCycle(self, head):
        if head is None or head.next is None:
           return None
        fast = slow = head
        met = False
        while fast and fast.next and slow:
              if not met:
                 fast = fast.next.next
                 slow = slow.next
                 if fast == slow:
                    met = True
                    slow = head
              else:
                 while slow != fast:
                       fast = fast.next
                       slow = slow.next
                 return slow
        return None
        

if __name__ == '__main__':
   s = Solution()
   test = ListNode(1)
   test.next = ListNode(2)
   test.next.next = ListNode(3)
   test.next.next.next = ListNode(4)
   test.next.next.next.next = test.next

   # test.next = test
   print s.detectCycle(test).val