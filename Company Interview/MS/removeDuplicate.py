def remove_duplicate(nums):
    if not nums or len(nums) == 1:
        return nums
    start = 1; end = len(nums) - 1
    nums.sort()
    while start <= end:
        if nums[start] != nums[start - 1]:
            start += 1
        else:
            del nums[start]
            end -= 1
    return nums

if __name__ == "__main__":
    nums = [1, 2, 1, 2, 3, 3, 2]
    print remove_duplicate(nums)
    nums = [1, 3, 4, 2, 5, 0]
    print remove_duplicate(nums)

