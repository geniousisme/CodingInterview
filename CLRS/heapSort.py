# bc: O(nlogn)
# ac: O(nlogn)
# wc: O(nlogn)

class HeapSort(object):
    def __init__(self):
        self.heap_size = 0

    def parent(self, idx):
        if idx == 1:
            return 0
        if idx % 2 == 0:
            return idx // 2 - 1
        else:
            return idx // 2

    def left(self, idx):
        return 2 * idx + 1

    def right(self, idx):
        return 2 * idx + 2

    def heapify(self, nums, idx, heap_size): #here is the max heapify
        l = self.left(idx)
        r = self.right(idx)
        largest = 0
        if l < heap_size and nums[l] > nums[idx]:
            largest = l
        else:
            largest = idx
        if r < heap_size and nums[r] > nums[largest]:
            largest = r
        if largest != idx:
            nums[idx], nums[largest] = nums[largest], nums[idx]
            self.heapify(nums, largest, heap_size)

    def build_max_heap(self, nums, heap_size):
        for i in xrange((heap_size - 1) / 2, -1, -1):
            self.heapify(nums, i, heap_size)

    def heap_sort(self, nums):
        self.heap_size = len(nums)
        self.build_max_heap(nums, self.heap_size)
        for i in xrange(self.heap_size - 1, -1, -1):
            nums[0], nums[i] = nums[i], nums[0]
            self.heapify(nums, 0, i)

if __name__ == "__main__":
    hs = HeapSort()
    nums = [4, 6, 2, 1, 7, 0, 12, 13, 9, 8, 5]
    hs.heap_sort(nums)
    print nums
