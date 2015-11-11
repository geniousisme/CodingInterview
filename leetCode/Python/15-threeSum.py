class Solution1:
    # @return a list of lists of length 3, [[val1,val2,val3]]
    # -4 -1 -1 0 1 2
    def slowerThreeSum(self, num_list):
        num_list = sorted(num_list)
        three_sum_comb = []; processed_dict = {}
        for idx, num in enumerate(num_list):
            if not processed_dict.get(num):
                tmp_sum_comb, tmp_dict = self.twoSum(num_list[idx + 1:], -num)
                processed_dict = dict(processed_dict, **tmp_dict)
                for sum_comb in tmp_sum_comb:
                    three_sum = [num] + sum_comb
                    if three_sum not in three_sum_comb:
                       three_sum_comb.append(three_sum)
        return three_sum_comb

    def twoSum(self, num_list, summation):
        num_idx_dict = {}; sum_combination = []; processed_dict = {}
        for idx, num in enumerate(num_list):
            if summation - num in num_idx_dict:
                sum_combination.append(                                 \
                                       [                                \
                                        num_list                        \
                                        [num_idx_dict[summation - num]],\
                                        num                             \
                                       ]                                \
                                      )
            num_idx_dict[num] = idx
            processed_dict[num] = True
        return sum_combination, processed_dict

    def threeSum(self, num_list):
        num_list = sorted(num_list)
        left = 0; right = len(num_list) - 1

'''
time:  O(N^2)
space: O(1)
1. sort nums
2. start from zero, and search for other nums with two ptr method which sum up as zero.
3. avoid repated
'''
# notice: this one has many detail, need to practice more!
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort() # sort the nums first
        res = []
        length = len(nums)
        for i in xrange(length - 2): # notice here is length - 2
            # avoid repeat
            if i == 0 or nums[i] > nums[i - 1]:
                start = i + 1; end = length - 1
                # two Sum for -nums[i]
                while start < end:
                    if nums[start] + nums[end] == -nums[i]:
                        res.append([nums[i], nums[start], nums[end]])
                        start += 1
                        end -= 1
                        # avoid repeat
                        while start < end and nums[end] == nums[end + 1]:
                            end -= 1
                        while start < end and nums[start] == nums[start - 1]:
                            start += 1
                    elif nums[start] + nums[end] > -nums[i]:
                        end -= 1
                    else:
                        start += 1
        return res

if __name__ == "__main__":
    import time
    start = time.clock()
    s = Solution()
    num = []
    print s.threeSum(num)
    num = [-1, 0, 1]
    print s.threeSum(num)
    num = [0, 0, 0]
    print s.threeSum(num)
    num = [-4,-2,1,-5,-4,-4,4,-2,0,4,0,-2,3,1,-5,0]
    print s.threeSum(num)
    print "%s sec" % (time.clock() - start)
