# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: bool
        """
        if not intervals:
            return True
        def get_interval_start_time(interval):
            return interval.start
        intervals = sorted(intervals, key=get_interval_start_time)
        for i in xrange(1, len(intervals)):
            if intervals[i - 1].end > intervals[i].start:
                return False
        return True

if __name__ == "__main__":
    s = Solution()
    print s.canAttendMeetings([[0, 30], [5, 10], [15, 20]])
