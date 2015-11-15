class Solution(object):
    '''
    TC: O(n ^ 2)
    SC: O(n)
    '''
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        dp = [1] * len(nums)
        max_len = 0
        for i in xrange(1, len(nums)):
            for j in xrange(i):
                if nums[i] >= nums[j]:
                    dp[i] = max(dp[j] + 1, dp[i])
                    max_len = max(max_len, dp[i])
        return dp[-1]

class Solution2(object):
    '''
    TC: O(nlogn)
    SC: O(n)
    '''
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        dp = [nums[0]]
        for i in xrange(1, len(nums)):
            if nums[i] > dp[-1]:
                dp.append(nums[i])
            else:
                dp[self.binary_search(dp, nums[i])] = nums[i]
        return len(dp)

    def binary_search(self, nums, target):
        start = 0; end = len(nums) - 1
        while start < end:
            mid = (start + end) / 2
            if nums[mid] < target:
                start = mid + 1
            else:
                end = mid
        return start

class Solution(object):
    '''
    TC: O(nlogn)
    SC: O(n)
    '''
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
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

    def search_insert_pos(self, nums, target):
        start = 0; end = len(nums) - 1
        while start + 1 < end:
            mid = (start + end) / 2
            if nums[mid] < target:
                start = mid
            elif nums[mid] > target:
                end = mid
            else:
                end = mid
        if nums[start] >= target:
            return start
        if nums[end] >= target:
            return end
        return len(nums)

if __name__ == "__main__":
    s = Solution()
    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    print s.lengthOfLIS(nums)
    nums = [2, 2]
    print s.lengthOfLIS(nums)
    nums = [1]
    print s.lengthOfLIS(nums)