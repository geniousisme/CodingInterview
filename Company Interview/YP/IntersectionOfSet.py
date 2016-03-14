# Intersection of Set
def intersection(set1, set2):
    '''
    Time:  O(n ^ 2)
    Space: O(1), result need O(n)
    '''
    inter_set = []
    if set1 and set2:
        for i1 in xrange(len(set1)):
            for i2 in xrange(len(set2)):
                if set2[i2] == set1[i1]:
                    inter_set.append(set2[i2])
    return inter_set

def intersection2(set1, set2):
    '''
    Time:  O(nlogn)
    Space: O(1), result need O(n)
    '''
    inter_set = []
    if set1 and set2:
        set1 = sorted(set1)
        set2 = sorted(set2)
        i1 = i2 = 0
        while i1 < len(set1) and i2 < len(set2):
            if set1[i1] == set2[i2]:
                inter_set.append(set1[i1])
                i1 += 1; i2 += 1
            elif set1[i1] < set2[i2]:
                i1 += 1
            else:
                i2 += 1
    return inter_set

def intersection3(set1, set2):
    '''
    Time:  O(n)
    Space: O(n), result need O(n)
    '''
    num_dict = {}; inter_set = []
    for num in set1 + set2:
        if num_dict.get(num):
            inter_set.append(num)
        else:
            num_dict[num] = 1
    return inter_set

if __name__ == "__main__":
    set1 = [7, 1, 5, 2, 3, 6]
    set2 = [3, 8, 6, 20, 7]
    print intersection(set1, set2)
    print intersection2(set1, set2)
    print intersection3(set1, set2)
