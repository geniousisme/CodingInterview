class Solution1:
    # @param {integer[]} nums
    # @return {integer[][]}
    def __init__(self):
        self.length = 0
    def permuteUnique(self, nums):
        res = []
        if nums:
           self.length = len(nums)
           nums.sort()
           visited = [False for i in xrange(self.length)]
           self.dfs(nums, [], 0, visited, res)
        return res

    def dfs(self, nums, perm, perm_len, visited, res):
        if perm_len == self.length:
           res.append(perm)
           return
        for i in xrange(self.length):
            if not visited[i]:
               if i > 0 and visited[i - 1] == False and nums[i - 1] == nums[i]:
                  continue
               visited[i] = True
               self.dfs(nums, perm + [nums[i]], perm_len + 1, visited, res)
               visited[i] = False

class Solution(object):
    # @param {integer[]} nums
    # @return {integer[][]}
    def __init__(self):
        self.length = 0
        self.res    = []
    
    def permuteUnique(self, nums):
        if nums:
            self.res = []
            self.length = len(nums)
            visited     = [False for i in xrange(self.length)]
            nums.sort() # notice!!! it must be there for checking duplicate!!
            self.perm_helper(nums, [], visited)
        return self.res

    def perm_helper(self, nums, perm, visited):
        if len(perm) == self.length:
            self.res.append(perm)
            return
        
        for i in xrange(self.length):
            if not visited[i]:
                if i > 0 and visited[i - 1] == False and nums[i] == nums[i - 1]:
                    continue
                visited[i] = True
                self.perm_helper(nums, perm + [nums[i]], visited)
                visited[i] = False

if __name__ == '__main__':
   s = Solution()
   print s.permuteUnique([-1, -1, 3, -1])
        