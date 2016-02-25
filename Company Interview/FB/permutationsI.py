class Solution(object):
    def permute(self, nums):
        '''
        Time:  O(n * n!)
        Space: O(n)

        use visited and left_nums to manage the repeated cases
        '''
        def permute_helper(left_nums, perm):
            if len(perm) == length:
                res.append(perm)
                return
            for i in xrange(len(left_nums)):
                permute_helper(left_nums[:i] + left_nums[i + 1:], perm + [left_nums[i]])
        res = []; length = len(nums)
        if nums:
            permute_helper(nums, [])
        return res

if __name__ == "__main__":
    s = Solution()
    print s.permute([1, 2, 3])
