class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def __init__(self):
        self.res = []
        self.length = 0 
    
    def subsets(self, nums):
        # nums.sort()
        self.length = len(nums)
        self.DFS([], 0, nums, 0)
        return self.res
        
    def DFS(self, comb, start, nums, depth): # optimized, use index but not whole list
        self.res.append(list(comb))
        if depth == self.length:  return
        for i in xrange(start, self.length):
            comb.append(nums[i])
            # self.DFS(comb + [nums[i]], i + 1, nums, depth + 1)
            self.DFS(comb, i + 1, nums, depth + 1)
            comb.pop()

if __name__ == '__main__':
   s = Solution()
   print s.subsets([1, 2, 3])