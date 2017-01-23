import collections


def snap_print():
    pass

def snap_diff(f1, f2):
    # print '=' * 50
    # f1 = map(str, f1)
    # f2 = map(str, f2)
    change_flag = False
    if len(f1) > len(f2):
        f1, f2 = f2, f1
        change_flag = True
    counter = collections.Counter(f1)

    for line in f2:
        if counter[line] == 0:
            print '-'+line if change_flag else '+'+line
        else:
            counter[line] -= 1
    for k, v in counter.iteritems():
        for _ in xrange(v):
            print '-' + line if change_flag else '+' + line


snap_diff(['A', 'B', 'C', 'D', 'E'], ['A', 'B', 'D'])
snap_diff([], [1])
snap_diff([2], [])
snap_diff([1,1,1], [1])
snap_diff([1], [1,1,1])
snap_diff([1,2,3,4,5], [3,6,7,9,2,10])