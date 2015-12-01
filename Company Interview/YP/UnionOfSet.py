def union(set1, set2):
    '''
    Time:  O(n ^ 2)
    Space: O(1)
    '''
    if not set1 and not set2:
        return []
    if not set1:
        return set2
    if not set2:
        return set1
    union_set = set1
    for num in set2:
        if num not in union_set:
            union_set.append(num)
    return union_set

def union2(set1, set2):
    '''
    Time:  O(nlogn)
    Space: O(1)
    '''
    if not set1 and not set2:
        return []
    if not set1:
        return set2
    if not set2:
        return set1
    union_set = []
    set1 = sorted(set1)
    set2 = sorted(set2)
    i1 = i2 = 0
    while i1 < len(set1) or i2 < len(set2):
        if i1 >= len(set1):
            union_set.extend(set2[i2:])
            break
        if i2 >= len(set2):
            union_set.extend(set1[i1:])
            break
        if set1[i1] == set2[i2]:
            union_set.append(set1[i1])
            i1 += 1; i2 += 1
        elif set1[i1] < set2[i2]:
            union_set.append(set1[i1])
            i1 += 1
        else:
            union_set.append(set2[i2])
            i2 += 1
    return union_set

def union3(set1, set2):
    if not set1 and not set2:
        return []
    if not set1:
        return set2
    if not set2:
        return set1
    num_dict = {}
    union_set = []
    for num in set1 + set2:
        if num_dict.get(num) is None:
            union_set.append(num)
            num_dict[num] = 1
    return union_set

if __name__ == "__main__":
    set1 = [7, 1, 5, 2, 3, 6]
    set2 = [3, 8, 6, 20, 7]
    print union(set1, set2)
    print union2(set1, set2)
    print union3(set1, set2)