class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        sum_dict = {}
        res      = set()
        num_len = len(nums)
        nums.sort()
        # get the two sum combinations first with idx ascending order
        for i in xrange(num_len):
            for j in xrange(i + 1, num_len):
                if sum_dict.get(nums[i] + nums[j]) is None:
                    sum_dict[nums[i] + nums[j]] = [(i, j)]
                else:
                    sum_dict[nums[i] + nums[j]].append((i, j))
        # similar to two Sum, we cut nums[i] & nums[j] from target, use the diff to find
        # if the diff is in sum combination or not, then store it into set to avoid repeatied situation
        for i in xrange(num_len):
            for j in xrange(i + 1, num_len - 2):
                # since we can hv two more elems from the left
                left = target - nums[i] - nums[j]
                if sum_dict.get(left) is not None:
                    for idx_tuple in sum_dict[left]:
                        if idx_tuple[0] > j:
                            res.add((nums[i], nums[j], nums[idx_tuple[0]], nums[idx_tuple[1]]))
        return [list(r) for r in res]

if __name__ == "__main__":
    s = Solution()
    print s.fourSum([-3,-2,-1,0,0,1,2,3], 0)



