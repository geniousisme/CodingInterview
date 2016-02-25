class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        Ugly nums can be seperated as following nms:
        (1) 1x2, 2x2, 3x2, 4x2, 5x2, ...
        (2) 1x3, 2x3, 3x3, 4x3, 5x3, ...
        (3) 1x5, 2x5, 3x5, 4x5, 5x5, ...
        pick the min elem from the three lists, then move the idx to next,
        repeat the process, once you get the nth element, stop
        """
        ugly_nums = [1]
        i2 = i3 = i5 = 0
        while len(ugly_nums) < n:
            min_elem = min(ugly_nums[i2] * 2, ugly_nums[i3] * 3, ugly_nums[i5] * 5)
            # notice: why use if for each case?
            #         which can avoid the repeated result, like 3 * 2 & 2 * 3
            #         then it will move forward together, will not contain two 6.
            if min_elem == ugly_nums[i2] * 2:
                i2 += 1
            if min_elem == ugly_nums[i3] * 3:
                i3 += 1
            if min_elem == ugly_nums[i5] * 5:
                i5 += 1
            ugly_nums.append(min_elem)
        return ugly_nums[-1]

if __name__ == "__main__":
    s = Solution()
    print s.nthUglyNumber(10)