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

if __name__ == '__main__':
    nums = [5,0,9,3,2,1,19,100]
    print mergeSort(nums)
    print sorted(nums)
  




