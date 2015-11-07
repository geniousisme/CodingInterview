class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        candidate1 = candidate2 = None
        count1 = count2 = 0
        for n in nums:
            if candidate1 == n:
                count1 += 1
            elif candidate2 == n:
                count2 += 1
            elif count1 == 0:
                candidate1 = n
                count1 = 1
            elif count2 == 0:
                candidate2 = n
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1
        res = []
        count1 = count2 = 0
        for n in nums:
            if n == candidate1:
                count1 += 1
            elif n == candidate2:
                count2 += 1
        if count1 > len(nums) / 3:
            res.append(candidate1)
        if count2 > len(nums) / 3:
            res.append(candidate2)

        return res

if __name__ == "__main__":
    s = Solution()
    print s.majorityElement([2, 2, 2, 2, 1, 1, 1, 1, 3, 3, 0])
    print s.majorityElement([2, 4, 1, 1])
