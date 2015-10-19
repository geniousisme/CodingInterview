class Pairs(object):
    def __init__(self, sum, idx):
        self.sum = sum
        self.idx = idx

class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers includes the index of the first number
             and the index of the last number
    """
    # spend too much time on this question, re-write it sometimes
    def subarraySumClosest(self, nums):
        # write your code here
        length = len(nums)
        pair_list = [Pairs(0, -1) for i in xrange(length + 1)]
        for i in xrange(1, length + 1):
            pair_list[i].sum = pair_list[i - 1].sum + nums[i - 1]
            pair_list[i].idx = i - 1
        pair_list = sorted(pair_list, key = lambda x: x.sum)
        # find the min diff & closet index
        min_diff  = 9999
        close_idx = -1
        for i in xrange(1, length + 1):
            if min_diff > abs(pair_list[i].sum - pair_list[i - 1].sum):
                min_diff  = abs(pair_list[i].sum - pair_list[i - 1].sum)
                close_idx = pair_list[i].idx
        left  = min(pair_list[close_idx].idx, pair_list[close_idx - 1].idx)
        right = max(pair_list[close_idx].idx, pair_list[close_idx - 1].idx)
        return [left, right]
if __name__ == "__main__":
    s = Solution()
    print s.subarraySumClosest( [-3, 1, 1, -3, 5])

