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
        dummy = ListNode(0)
        current, carry = dummy, 0

        while l1 is not None or l2 is not None:
            val = carry
            if l1 is not None:
                val += l1.val
                l1 = l1.next
            if l2 is not None:
                val += l2.val
                l2 = l2.next
            carry, val = val / 10, val % 10
            current.next = ListNode(val)
            current = current.next

        if carry == 1:
            current.next = ListNode(1)

        return dummy.next
