import heapq

class Solution(object):
    def kClosestPoint(self, points, target_point, k):
        heap = []
        for point in points:
            heapq.heappush(heap, (self.distance(point, target_point), point))
        for i in xrange(k):
            print heapq.heappop(heap)[1]

    def distance(self, point1, point2):
        return (point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2

if __name__ == "__main__":
    s = Solution()
    points = [(-2, -4), (0, 0), (10, 15), (5, 6), (7, 8), (-10, -30)]
    target_point = (5, 5)
    s.kClosestPoint(points, target_point, 2)
