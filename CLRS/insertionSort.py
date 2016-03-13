class InsertionSort(object):
    def insertion_sort(self, nums):
        for i in xrange(len(nums)):
            insert_elem = nums[i]
            insert_idx  = i
            while insert_idx > 0 and nums[insert_idx - 1] > insert_elem:
                nums[insert_idx] = nums[insert_idx - 1]
                insert_idx -= 1
            nums[insert_idx] = insert_elem
        return nums

if __name__ == "__main__":
    IS = InsertionSort()
    print IS.insertion_sort([18,5,3,1,19,6,0,7,4,2,5])