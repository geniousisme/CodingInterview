class Solution(object):
    # @param num, a list of integer
    # @return an integer
    def longestConsecutive(self, nums):
        result = 0; lengths = {num: 0 for num in nums}

        for num in nums:
            if lengths[num] == 0:
                lengths[num] = 1
                left, right = lengths.get(num - 1, 0), lengths.get(num + 1, 0)
                length = 1 + left + right
                result = max(result, length)
                lengths[num - left]  = length
                lengths[num + right] = length
        return result

if __name__ == "__main__":
    s = Solution()
    print s.longestConsecutive([100, 1, 2, 3, 4, 101])
