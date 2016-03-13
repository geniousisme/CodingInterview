# Reverse a singly linked list.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def print_llst(head):
    llst = ""
    while head:
          llst += str(head.val)
          if head.next:
             llst += '->'
          head = head.next
    print llst

'''
Time:  O(n)
Space: O(1)
'''
class Solution(object): # iterative
    def reverse(self, head):
        start = None
        return self.reverse_helper(head, start) 

    def reverse_helper(self, head, start):
        if head is None:
            return start
        next = head.next
        head.next = start
        return self.reverse_helper(next, head)

'''
Time:  O(n)
Space: O(1)
'''
class Solution(object): # recursive
    def reverseList(self, head):
        return self.reverse_helper(head, None)

    def reverse_helper(self, head, start):
        if head is None:
            return start
        else:
            nxt = head.next
            head.next = start
            return self.reverse_helper(nxt, head)

if __name__ == '__main__':
   s = Solution()
   test = ListNode(1)
   test.next = ListNode(2)
   test.next.next = ListNode(3)
   test.next.next.next = ListNode(4)
   test.next.next.next.next = ListNode(5)

   print_llst(s.reverse(test))
