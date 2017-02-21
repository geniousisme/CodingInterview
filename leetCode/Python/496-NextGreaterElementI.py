class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        next_greater_dict = {}
        stack = []
        for n in nums:
            while stack and stack[-1] < n:
                next_greater_dict[stack.pop()] = n
            stack.append(n)
        return [next_greater_dict.get(n, -1) for n in findNums]