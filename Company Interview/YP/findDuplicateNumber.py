# Given an array nums containing n + 1 integers where each integer
# is between 1 and n (inclusive), prove that at least one duplicate number must exist.
# Assume that there is only one duplicate number, find the duplicate one.

# Note:
# You must not modify the array (assume the array is read only).
# You must use only constant, O(1) extra space.
# Your runtime complexity should be less than O(n2).
# There is only one duplicate number in the array, but it could be repeated more than once.
class Solution(object):
    def findDuplicate(self, nums):
        '''
        Time:  O(n)
        Space: O(1)
        '''
        slow = nums[0]
        fast = nums[nums[0]]
        while fast != slow:
            slow = nums[slow]
            fast = nums[nums[fast]]
        fast = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow

class Solution1(object):
    def findDuplicate(self, nums):
        """
        Time:  O(n)
        Space: O(1)
        Drawback: will change the original data structure
        """
        for num in nums:
            if nums[abs(num) - 1] > 0:
                nums[abs(num) - 1] *= -1
            else:
                duplicate = abs(num)
                break
        for num in nums:
            if nums[abs(num) - 1] < 0:
                nums[abs(num) - 1] *= -1
            else:
                break
        return duplicate

if __name__ == "__main__":
    s = Solution()
    print s.findDuplicate([2, 2, 2, 2, 2])
    print s.findDuplicate([1, 2, 5, 1, 3, 1])
