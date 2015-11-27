# Given two 1d vectors,
# implement an iterator to return their elements alternately.

# For example, given two 1d vectors:
# v1 = [1, 2]
# v2 = [3, 4, 5, 6]
# By calling next repeatedly until hasNext returns false,
# the order of elements returned by next should be: [1, 3, 2, 4, 5, 6].

# Follow up: What if you are given k 1d vectors?
# How well can your code be extended to such cases?


import collections
class ZigzagIterator(object):
    '''
    Time:  O(n)
    Space: O(n)
    '''
    def __init__(self, v1, v2):
        self.dq = collections.deque([(len(v), iter(v)) for v in (v1, v2) if v])

    def next(self):
        length, iterator = self.dq.popleft()
        if length > 1:
            self.dq.append((length - 1, iterator))
        return next(iterator)

    def hasNext(self):
        return bool(self.dq)

if __name__ == "__main__":
    zi = ZigzagIterator([1, 2], [3, 4, 5, 6])
    while zi.hasNext():
        print zi.next()
