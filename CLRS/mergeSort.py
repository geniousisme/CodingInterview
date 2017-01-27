from datetime import datetime 
import random
import Queue

from threading import Thread

def mergeSort(nums):
    length = len(nums)
    if length == 1:
        return nums
    mid   = length // 2
    left  = mergeSort(nums[:mid])
    right = mergeSort(nums[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    llen   = len(left)
    rlen   = len(right)
    lIdx   = rIdx = 0
    while lIdx < llen and rIdx < rlen:
        if left[lIdx] < right[rIdx]:
            result.append(left[lIdx])
            lIdx += 1
        else:
            result.append(right[rIdx])
            rIdx += 1
    if lIdx < llen:
        result.extend(left[lIdx:])
    else:
        result.extend(right[rIdx:])
    return result

class MultiThreadMergeSort(object):

    def merge(self, nums, start, mid, end):
        L = nums[start:mid]
        R = nums[mid:end]
        i = j = 0
        k = start
        for l in xrange(k, end):
            if j >= len(R) or (i < len(L) and L[i] < R[j]):
                nums[l] = L[i]
                i = i + 1
            else:
                nums[l] = R[j]
                j = j + 1  

    def merge_sort(self, nums, left, right):
        if right - left > 1:
            mid = int((left + right) / 2)

            threads = []
            thrd1 = Thread(
                target=self.merge_sort, name="Thrd-1", args=(nums, left, mid)
            )
            thrd2 = Thread(
                target=self.merge_sort, name="Thrd-2", args=(nums, mid, right)
            )

            thrd1.start()
            thrd2.start()

            threads.append(thrd1)
            threads.append(thrd2)

            for thread in threads:
                thread.join()

            self.merge(nums, left, mid, right)

if __name__ == '__main__':
    nums = [random.randint(0, 1000000) for i in xrange(100000)]
    
    start_time = datetime.now()
    mergeSort(nums)
    print "not multi-thread time: ", datetime.now() - start_time

    multi_thrd_merge_sort = MultiThreadMergeSort()
    
    start_time = datetime.now()
    multi_thrd_merge_sort.merge_sort(nums, 0, len(nums))
    print "multi-thread time: ", datetime.now() - start_time




