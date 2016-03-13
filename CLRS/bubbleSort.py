'''
bc: O(n), when nums is already sorted.
ac: O(n^2)
wc: O(n^2)
'''

class BubbleSort(object):
    def bubble_sort(self, nums):
        for end in xrange(len(nums) - 1, 0, -1):
            for i in xrange(1, end + 1):
                if nums[i - 1] > nums[i]:
                    self.swap(nums, i - 1, i)
        return nums

    def swap(self, nums, idx1, idx2):
        nums[idx1] = nums[idx1] ^ nums[idx2]
        nums[idx2] = nums[idx2] ^ nums[idx1]
        nums[idx1] = nums[idx2] ^ nums[idx1]

if __name__ == "__main__":
    bs = BubbleSort()
    print bs.bubble_sort([18,5,3,1,19,6,0,7,4,2,5])