class Solution(object):
    def permuteUnique(self, nums):
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
                if visited[i] or (i > 0 and not visited[i - 1] and left_nums[i] == left_nums[i - 1]): # notice!
                    continue
                visited[i] = True
                permute_helper(left_nums, perm + [left_nums[i]])
                visited[i] = False
        res = []; length = len(nums); visited = [False] * length
        if nums:
            permute_helper(sorted(nums), [])
        return res

if __name__ == "__main__":
    s = Solution()
    print s.permuteUnique([1, 1, 2])

