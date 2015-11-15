# Time:  O(nlogn)
# Space: O(n)
#
# Given an unsorted array of integers,
# find the length of longest increasing subsequence.
#
# For example,
# Given [10, 9, 2, 5, 3, 7, 101, 18],
# The longest increasing subsequence is [2, 3, 7, 101],
# therefore the length is 4. Note that there may be more
# than one LIS combination, it is only necessary for you to return the length.
#
# Your algorithm should run in O(n2) complexity.
#
# Follow up: Could you improve it to O(n log n) time complexity?
#

class Solution1(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        TC: O(n ^ 2)
        SC: O(n)
        """
        if not nums:
            return 0
        # dp table i: the max length of increasing sequence from 0 to i
        dp = [1] * len(nums)
        max_len = 0
        # now we compare i with its previous elems
        for i in xrange(1, len(nums)):
            for j in xrange(i):
                # if there is some increasing order, we find which one is bigger:
                # dp[i] or dp[j + 1]
                if nums[i] > nums[j]:
                    dp[i] = max(dp[j] + 1, dp[i])
                    # and compare the dp[i] length with the current max length
                    max_len = max(dp[i], max_len)
        return max_len

class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        TC: O(nlogn)
        SC: O(n)
        """
        if not nums:
            return 0
        dp = [nums[0]]
        for i in xrange(1, len(nums)):
            insert_pos = self.search_insert_pos(dp, nums[i])
            if insert_pos >= len(dp):
                dp.append(nums[i])
            else:
                dp[insert_pos] = nums[i]
        return len(dp)

    # see the definition of the search insert position question on leetcode
    def search_insert_pos(self, dp, target):
        # find the left boundry question
        start = 0; end = len(dp) - 1
        while start + 1 < end:
            mid = (end + start) / 2
            if dp[mid] > target:
                end = mid
            elif dp[mid] < target:
                start = mid
            else:
                end = mid
        if dp[start] >= target:
            return start
        if dp[end] >= target:
            return end
        return len(dp)

if __name__ == "__main__":
    s = Solution()
    print s.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18])



