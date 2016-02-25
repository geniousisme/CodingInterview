class Solution(object):
    def subarraySum(self, nums, target):
        '''
        Time:  O(n)
        Space: O(1)
        '''
        if target < 1 or not nums: # notice the boundry condition
            return False
        start = end = 0; sum = 0
        while end < len(nums):
            while end < len(nums) and sum < target:
                sum += nums[end]
                if sum == target:
                    return True
                else:
                    end += 1
            while start < end and sum > target:
                sum -= nums[start]
                if sum == target:
                    return True
                else:
                    start += 1
        return False

if __name__ == "__main__":
    s = Solution()
    nums = [2,3,1,2,4,3]
    print s.subarraySum([2,3,1,2,4,3], 7)
    print s.subarraySum([2,3,1,2,4,3], 8)
    print s.subarraySum([2,3,1,2,4,3], 9)
    print s.subarraySum([2,3,1,2,4,3], 0)
    print s.subarraySum([2,3,1,2,4,3], 99)



