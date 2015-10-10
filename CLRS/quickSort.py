import random

def quicksortInPlace(nums, start, end): # in-place version
    if start > end:
        return
    pivot = random.choice(nums)
    left  = start
    right = end
    while left <= right:
        while nums[left] < pivot:
            left += 1
        while nums[right] > pivot:
            right -= 1
        if left <= right:
            swap(nums, left, right)
            left  += 1
            right -= 1
    quicksort(nums, left,  end  )
    quicksort(nums, start, right)

def swap(nums, left, right):
    nums[left], nums[right] = nums[right], nums[left]

def quicksort(nums): # additional space
    if not nums:
       return nums
    left      = []
    right     = []
    pivotList = []
    pivot     = random.choice(nums)
    for n in nums:
        if n < pivot:
           left.append(n)
        elif n > pivot:
           right.append(n)
        else:
           pivotList.append(n)
    return quicksort(left) + pivotList + quicksort(right)

if __name__ == '__main__':
   nums = [2, 4, 7, 8, 1, 3, 10, 9, 6, 5]
   # quicksort(nums, 0, len(nums) - 1)

   print nums
   print quicksort(nums)
