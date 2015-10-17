'''
time:  O(N**2)
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
        # notice here is length - 2,
        # since we will get two more(aka start, end) from the left.
        for i in xrange(length - 2):
            # avoid repeat
            if i == 0 or nums[i] > nums[i - 1]:
                start = i + 1; end = length - 1 # two Sum for -nums[i]
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
    s = Solution()
    print s.threeSum([-1, 0, 1, 2, -1, -4])
    print s.threeSum([0, 0, 0, 0])


