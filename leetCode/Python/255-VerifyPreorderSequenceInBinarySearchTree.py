# Given an array of numbers,
# verify whether it is the correct preorder traversal sequence of a binary search tree.
# You may assume each number in the sequence is unique.

# Follow up:
# Could you do it using only constant space complexity?

class Solution1(object):
    '''
    Time:  O(n)
    Space: O(n)
    '''
    def verifyPreorder(self, preorder):
        # use inorder list to maintain the inorder sequence for BST
        inorder_list = []
        # use stack to store the elements we have now
        stack        = []
        for p in preorder:
            # since bst inorder sequence should be ascending, then if the last element of inorder list
            # is bigger than latest element we iterate, then return False
            if inorder_list and inorder_list[-1] > p:
                return False
            # if the element we iterate now is bigger than the last element
            while stack and p > stack[-1]:
                # put them to inorder list
                inorder_list.append(stack.pop())
            # otherwise, store the rest of element into stack
            stack.append(p)
        return True

class Solution2(object):
    '''
    Time:  O(n)
    Space: O(n)
    For this solution, we use low to represent the last element of inorder list
    '''
    def verifyPreorder(self, preorder):
        low = None
        stack = []
        for p in preorder:
            if low is not None and low > p:
                return False
            while stack and p > stack[-1]:
                low = stack.pop()
            stack.append(p)
        return True

class Solution(object):
    '''
    Time:  O(n)
    Space: O(1)
    '''
    def verifyPreorder(self, preorder):
        low = None
        idx = -1
        for p in preorder:
            if low is not None and low > p:
                return False
            while idx >= 0 and preorder[idx] < p:
                low = preorder[idx]
                idx -= 1
            # use idx to similuate the process of putting the element into stack
            # continue comparing to the last elem.
            idx += 1
            preorder[idx] = p
        return True


if __name__ == "__main__":
    s2 = Solution2()
    print s2.verifyPreorder([9, 5, 1, 6, 13, 10, 15])
    s1 = Solution1()
    print s1.verifyPreorder([9, 5, 1, 6, 3, 13, 10, 15])
    s = Solution()
    print s.verifyPreorder([9, 5, 1, 6, 10, 15])


