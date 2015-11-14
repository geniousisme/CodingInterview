class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.sums = []
        if nums:
            self.sums.append(nums[0])
            for i in xrange(1, len(nums)):
                self.sums.append(nums[i] + self.sums[i - 1])

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        if not self.sums:
            return 0
        if i == 0:
            return self.sums[j]
        return self.sums[j] - self.sums[i - 1]


if __name__ == "__main__":
    s = NumArray([-2, 0, 3, -5, 2, -1])
    print s.sumRange(0, 2)
    print s.sumRange(2, 5)
    print s.sumRange(0, 5)

