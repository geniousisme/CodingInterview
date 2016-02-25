class CountingSort(object):
    def __init__(self):
        self.max_val = 0
        self.length  = 0

    def count_sort(self, nums):
        if nums:
            self.max_val = max(nums)
            self.length  = len(nums)
            count = [0 for i in xrange(self.max_val + 1)]
            for n in nums:
                count[n] += 1
            i = 0; count_idx = 0
            while i < self.length and count_idx < self.max_val + 1:
                if count[count_idx] == 0:
                    count_idx += 1
                else:
                    nums[i] = count_idx
                    count[count_idx] -= 1
                    i += 1
        return nums

if __name__ == "__main__":
    cs = CountingSort()
    nums = [7, 8, 10, 3, 2, 1, 5, 4, 1, 2, 2, 3, 3, 3, 4, 4, 9, 9, 0]
    print nums
    print cs.count_sort(nums)
