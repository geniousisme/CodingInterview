'''
bc: O(n^2)
ac: O(n^2)
wc: O(n^2)
'''

class SelectionSort(object):
    def selection_sort(self, nums):
        length = len(nums)
        for end in xrange(length - 1, 0, -1):
            max_idx  = 0
            for i in xrange(1, end + 1):
                if nums[i] > nums[max_idx]:
                    max_idx  = i
            self.swap(nums, max_idx, end)
        return nums

    def swap1(self, nums, idx1, idx2):
        nums[idx1], nums[idx2] = nums[idx2], nums[idx1]

    def swap(self, nums, idx1, idx2):
        nums[idx1] = nums[idx1] ^ nums[idx2]
        nums[idx2] = nums[idx1] ^ nums[idx2]
        nums[idx1] = nums[idx2] ^ nums[idx1]

if __name__ == "__main__":
    ss = SelectionSort()
    print ss.selection_sort([18,5,3,1,19,6,0,7,4,2,5])