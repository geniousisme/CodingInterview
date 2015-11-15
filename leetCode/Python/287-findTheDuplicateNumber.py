# Given an array nums containing n + 1 integers where each integer
# is between 1 and n (inclusive), prove that at least one duplicate
# element must exist. Assume that there is only one duplicate number,
# find the duplicate one.
#
# Note:
# - You must not modify the array (assume the array is read only).
# - You must use only constant extra space.
# - Your runtime complexity should be less than O(n^2).
#

# Two pointers method, same as Linked List Cycle II.

class Solution(object):
    def findDuplicate(self, nums):
        # Time:  O(n)
        # Space: O(1)

        # Treat each (key, value) pair of the array as the (pointer, next) node of the linked list,
        # thus the duplicated number will be the begin of the cycle in the linked list.
        # Besides, there is always a cycle in the linked list which
        # starts from the first element of the array.
        slow = nums[0]
        fast = nums[nums[0]]
        while fast != slow:
            slow = nums[slow]       # ptr.next
            fast = nums[nums[fast]] # ptr.next.next
        # but in [1, 3, 4, 2, 2] case, it might ends up with 4, not 2
        # so need to iterate from beginning again to find the value
        fast = 0
        # if the two ptr meet, then quit and return slow
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow

class Solution1(object):
    def findDuplicate(self, nums):
        # Time:  O(nlogn)
        # Space: O(1)

        # binary search solution
        start = 1; end = len(nums) - 1
        # use binary search to find the left boundry
        # ex. 1 3 4 2 2, mid = 2, count = 3, which means mid is too big(more than 2.5, the half of length)
        # then end should be mid - 1 to find the left boundry; on the other hand, in the next round
        # we know that mid = 1(start = 1, end = 1),
        # then it is too small to find the duplicate, so start = mid + 1
        # then we get the duplicate value
        while start <= end:
            mid   = start + (end - start) / 2
            count = 0
            for num in nums:
                if mid >= num:
                    count += 1
            if count > mid:
                end = mid - 1
            else:
                start = mid + 1
        return start

class Solution2(object):
    def findDuplicate(self, nums):
        # Time: O(n)
        # Space: O(n)

        # mark the visited element as negative
        duplicate = None
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
    print s.findDuplicate([1, 3, 4, 2, 2])
