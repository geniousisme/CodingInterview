class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        for n in nums:
            if count == 0:
                candidate = n
            if candidate != n:
                count -= 1
            else:
                count += 1
        return candidate

if __name__ == "__main__":
    s = Solution()
    print s.majorityElement([2, 2, 2, 1, 1, 1, 2])
    print s.majorityElement([2, 2, 2, 1, 1, 1, 1])
