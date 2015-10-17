class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers includes the index of the first number 
             and the index of the last number
    """
    # time complexity: O(N ^ 2)
    # space complexity: O(1)
    def subarraySumI(self, nums):
        length = len(nums)
        for i in xrange(length):
            sum = 0
            for j in xrange(i, length): # notice for reapted index, like [0] -> [0, 0]
                sum += nums[j]
                if sum == 0:
                    return [i, j]
        return []
    # time complexity: O(N)
    # space complexity: O(N)
    def subarraySum(self, nums):
        sum_idx_hash = {0:-1}
        sum = 0
        for i in xrange(len(nums)):
            sum += nums[i]
            if sum_idx_hash.get(sum) is not None:
                return [sum_idx_hash[sum] + 1, i]
            sum_idx_hash[sum] = i
        return []

if __name__ == "__main__":
    s = Solution()
    print s.subarraySum([-3, 1, 2, -3, 4])
    print s.subarraySum([0])

