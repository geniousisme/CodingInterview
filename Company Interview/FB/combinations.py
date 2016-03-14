class Solution(object):
    '''
    Time:  O(n!)
    Space: O(n)

    use left_nums to have the rest of element to join the combinations
    '''
    def combinations(self, nums, k):
        def comb_helper(comb, left_nums):
            if len(comb) == k:
                res.append(comb)
                return
            for i in xrange(len(left_nums)):
                comb_helper(comb + [left_nums[i]], left_nums[i + 1:])
        res = []
        if nums:
            comb_helper([], nums)
        return res

if __name__ == "__main__":
    s = Solution()
    print s.combinations([1, 2, 3, 4], 2)
