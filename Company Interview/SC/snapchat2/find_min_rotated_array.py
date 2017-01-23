def find_min(a):
    """
    Duplication is allowed in array a
    """
    low, high = 0, len(a)-1
    while low < high:
        mid = (low+high) / 2
        if a[mid] > a[high]:
            low = mid + 1
        elif a[mid] < a[high]:
            high = mid
        else:
            high -= 1
    return a[low]



assert find_min([1,2,3,4,5]) == 1
assert find_min([3,4,5,1,2]) == 1
assert find_min([2,3,4,5,1]) == 1
assert find_min([5,1,2,3,4]) == 1
assert find_min([4,5,1,2,3]) == 1
assert find_min([1]) == 1
# assert find_min([]) == 1
#
#
assert find_min([1,5,5,5,5]) == 1
assert find_min([5,1,5,5,5]) == 1
assert find_min([5,5,1,5,5]) == 1
assert find_min([5,5,5,1,5]) == 1
assert find_min([5,5,5,5,1]) == 1