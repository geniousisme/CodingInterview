class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end   = e

class Solution(object):
    def minMeetingRoom(self, intervals):
        starts, ends = [], []
        s, e = 0, 0
        min_rooms = count_rooms = 0
        for interval in intervals:
            starts.append(interval.start)
            ends.append(interval.end)

        while s < len(starts):
            if starts[s] < ends[e]:
                count_rooms += 1
                min_rooms = max(min_rooms, count_rooms)
                s += 1
            else:
                count_rooms -= 1
                e += 1

        return min_rooms

if __name__ == "__main__":
    s = Solution()
    print s.minMeetingRoom([Interval(0, 30), Interval(1, 15), Interval(10, 30), Interval(40, 50)])