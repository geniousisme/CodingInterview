class BinarySearchTemplate(object):
    def binary_search_iter(self, nums, target): # iterative
        if not nums:
            return -1
        start = 0; end = len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start) / 2
            if nums[mid] < target:
                start = mid
            elif nums[mid] > target:
                end = mid
            else:
                return mid
        if nums[start] == target:
            return start
        if nums[end] == target:
            return end
        return -1

    def binary_search_rec(self, nums, target): # recursive, not recommended
        if not nums:
            return -1
        return self.binary_search_rec_helper(nums, 0, len(nums) - 1, target)

    def binary_search_rec_helper(self, nums, start, end, target):
        if start + 1 >= end:
            if nums[start] == target:
                return start
            if nums[end] == target:
                return end
            return -1
        mid = start + (end - start) / 2
        if nums[mid] > target:
            return self.binary_search_rec_helper(nums, start, mid, target)
        elif nums[mid] < target:
            return self.binary_search_rec_helper(nums, mid,   end, target)
        else:
            return mid


if __name__ == "__main__":
    bst = BinarySearchTemplate()
    print bst.binary_search_rec([1], 1)
    print bst.binary_search_rec([1, 2, 4, 5, 7, 9, 10], 4)
    print bst.binary_search_rec([1, 2, 4, 5, 7, 9, 10], 1)
    print bst.binary_search_rec([1, 2, 4, 5, 7, 9, 10], 10)
    print bst.binary_search_rec([1, 2, 4, 5, 7, 9, 10], 11)
    print bst.binary_search_rec([1, 2, 4, 5, 7, 9, 10], 0)




