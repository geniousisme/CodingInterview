class SelectionSort(object):
    def selection_sort(self, nums):
        length = len(nums)
        last = length - 1
        curr_max = -999
        max_idx  = 0
        for end in xrange(length, -1, -1):
            for i in xrange(end):
                if nums[i] > curr_max:
                    curr_max = nums[i]
                    max_idx  = i
            self.swap(nums, max_idx, end)
        return nums

    def swap(self, nums, idx1, idx2):
        nums[idx1] ^= nums[idx2]
        nums[idx2] ^= nums[idx1]
        nums[idx1] ^= nums[idx2]

if __name__ == "__main__":
    ss = SelectionSort()
    print ss.selection_sort([18,5,3,1,19,6,0,7,4,2,5])