# Time:  O(n)
# Space: O(1)
#
# You are given two linked lists representing two non-negative numbers. 
# The digits are stored in reverse order and each of their nodes contain a single digit.
# Add the two numbers and return it as a linked list.
#
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
#
# Definition for singly-linked list.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class linkedList:
    def __init__(self):
        self.head = None

    def addNode(self, value):
        newNode = ListNode(value)
        newNode.next = self.head
        self.head = newNode

    def printList(self):
        node = self.head
        while node:
            print node.val
            node = node.next

class Solution1:
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
        lstSum = self.getNumInLst(l1) + self.getNumInLst(l2)
        numStrList = list(str(lstSum))
        finalLst = linkedList()
        for ns in numStrList:
            finalLst.addNode(int(ns))
        return finalLst.head

    def getNumInLst(self, node):
        tmpStr = ""
        while node:
              tmpStr = str(node.val) + tmpStr
              node   = node.next
        return int(tmpStr)

class Solution(object):
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode(-1)
        carry = 0; curr = dummy
        while l1 is not None and l2 is not None:
            sum = l1.val + l2.val + carry
            carry = sum // 10
            digit  = sum % 10
            curr.next = ListNode(digit)
            curr = curr.next
            l1 = l1.next
            l2 = l2.next
        while l1:
            sum = l1.val + carry
            carry = sum // 10
            digit  = sum % 10
            curr.next = ListNode(digit)
            curr = curr.next
            l1 = l1.next
        while l2:
            sum = l2.val + carry
            carry = sum // 10
            digit  = sum % 10
            curr.next = ListNode(digit)
            curr = curr.next
            l2 = l2.next
        if carry:
            curr.next = ListNode(carry)
            curr = curr.next
        return dummy.next

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
    l1 = ListNode(5)
    # l1.next = ListNode(4)
    # l1.next.next = ListNode(3)
    # l1.next.next.next = ListNode(2)
    l2 = ListNode(5)
    # l2.next = ListNode(6)
    # l2.next.next = ListNode(4)
    s.print_llst(s.addTwoNumbers(l1, l2))