# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        TC: O(N), the interval can be inserted directly,
                  here just use sort module to simplify the code
        SC: O(N)
        """
        intervals.append(newInterval)
        intervals = sorted(intervals, key=lambda x: x.start)
        res = [intervals[0]]
        for i in xrange(1, len(intervals)):
            if res[-1].end >= intervals[i].start >= res[-1].start:
                res[-1].end = max(res[-1].end, intervals[i].end)
            else:
                res.append(intervals[i])
        return res
