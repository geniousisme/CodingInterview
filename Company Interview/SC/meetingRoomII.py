# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution1(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int

        TC: O(nlogn)
        SC: O(n)
        """
        start_times = []
        end_times = []

        for interval in intervals:
            start_times.append(interval.start)
            end_times.append(interval.end)

        start_times.sort()
        end_times.sort()

        si = ei = 0
        room_count = 0
        min_room_num = 0
        while si < len(intervals):
            # Means need one more room in this period, since there is a meeting on-going.
            if start_times[si] < end_times[ei]:
                room_count += 1 # Need one more room
                min_room_num = max(min_room_num, room_count) # Check if current room number is avaible or not
                si += 1
            # Means we don't need room in this period, since one meeting is over
            else:
                room_count -= 1
                ei += 1
        return min_room_num