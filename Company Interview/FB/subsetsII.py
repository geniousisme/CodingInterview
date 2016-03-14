class Solution(object):
    '''
    Time:  O(n * 2 ^ n)
    Space: O(2 ^ n)

    use start to control the next value to visit
    if repeated, check the previous one
    '''
    def subsets(self, nums):
        def subset_helper(comb, start):
            res.append(comb)
            if len(comb) == length:
                return
            for i in xrange(start, length):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                subset_helper(comb + [nums[i]], i + 1)

        res = []; length = len(nums)
        if nums:
            nums = sorted(nums) # notice!
            subset_helper([], 0)
        return res

if __name__ == "__main__":
    s = Solution()
    print s.subsets([1, 1, 2])