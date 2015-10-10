class Solution1:
    # @param num, a list of integer
    # @return a list of lists of integers
    def __init__(self):
        self.length = 0
        self.res    = []

    def permute(self, num):
        if not num: return num
        if len(num) == 1: return [num]
        self.length = len(num)
        self.DFS([], num)
        return self.res

    def DFS(self, perm, left_num):
        if len(perm) == self.length:
           self.res.append(perm)
           return self.res
        for i in xrange(len(left_num)):
            self.DFS(perm + [left_num[i]], left_num[:i] + left_num[i + 1:])

class Solution(object):
    def __init__(self):
        self.res = []
        self.length = 0
    
    def permute(self, nums):
        self.res = []
        if nums:
            self.length = len(nums) # notice: it should be put here if nums is None
            self.permute_helper(nums, [])
        return self.res

    def permute_helper(self, nums, perm):
        if len(perm) == self.length:
            self.res.append(perm)
            return
        for i in xrange(len(nums)):
            self.permute_helper(nums[:i] + nums[i + 1:], perm + [nums[i]])
  
if __name__ == '__main__':
   s = Solution()
   num = [1, 2, 3]
   print s.permute(num)



