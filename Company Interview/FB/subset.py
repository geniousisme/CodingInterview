class Solution1(object):
    '''
    Time:  O(n * 2 ^ n)
    Space: O(2 ^ n)

    use start to visit the next rest of the element
    '''
    def subsets(self, nums):
        def subset_helper(sub, start):
            res.append(sub)
            if len(sub) == length:
                return
            for i in xrange(start, len(nums)):
                subset_helper(sub + [nums[i]], i + 1)
        res = []; length = len(nums)
        if nums:
            nums = sorted(nums)
            subset_helper([], 0)
        return res


if __name__ == "__main__":
    s = Solution()
    print s.subsets([1, 2, 3])
    print s.subsets([4, 1, 0])
