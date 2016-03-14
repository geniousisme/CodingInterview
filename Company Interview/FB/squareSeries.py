class Solution(object):
    def squareSeries(self, nums):
        positive_start = self.find_positive_idx(nums)
        if positive_start == 0:
            while positive_start < len(nums):
                print (nums[positive_start]) ** 2
                positive_start += 1
        elif positive_start == -1:
            positive_start = len(nums) - 1
            while positive_start >= 0:
                print (nums[positive_start]) ** 2
                positive_start -= 1
        else:
            negative_start = positive_start - 1
            while negative_start >= 0 and positive_start < len(nums):
                if abs(nums[negative_start]) < abs(nums[positive_start]):
                    print (nums[negative_start]) ** 2
                    negative_start -= 1
                elif abs(nums[negative_start]) > abs(nums[positive_start]):
                    print (nums[positive_start]) ** 2
                    positive_start += 1
                else:
                    print (nums[positive_start]) ** 2
                    print (nums[negative_start]) ** 2
                    positive_start += 1
                    negative_start -= 1
            if negative_start == -1:
                while positive_start < len(nums):
                    print (nums[positive_start]) ** 2
                    positive_start += 1
            if positive_start == len(nums):
                while  negative_start >= 0:
                    print (nums[negative_start]) ** 2
                    negative_start -= 1

    def find_positive_idx(self, nums):
        start = 0; end = len(nums) - 1
        while start + 1 < end:
            mid = (end + start) / 2
            if nums[mid] >= 0:
                end = mid
            else:
                start = mid
        if nums[start] >= 0:
            return start
        if nums[end] >= 0:
            return end
        return -1

if __name__ == "__main__":
    s = Solution()
    print s.squareSeries([-3, -1, 0, 1, 2, 4, 5])
    print s.squareSeries([-10, -8, -2, -1])
    print s.squareSeries([1, 2, 3, 4, 5])


