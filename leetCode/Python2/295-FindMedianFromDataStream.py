from heapq import *
class MedianFinder:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.minHeap = []
        self.maxHeap = []

    def addNum(self, num):
        """
        Adds a num into the data structure.
        :type num: int
        :rtype: void
        """
        heappush(self.maxHeap, -num)
        minTop = self.minHeap[0] if len(self.minHeap) else None
        maxTop = self.maxHeap[0] if len(self.maxHeap) else None
        if minTop < -maxTop or len(self.minHeap) + 1 < len(self.maxHeap):
            heappush(self.minHeap, -heappop(self.maxHeap))
        if len(self.maxHeap) < len(self.minHeap):
            heappush(self.maxHeap, -heappop(self.minHeap))
        print "minHeap", self.minHeap
        print "maxHeap", self.maxHeap

    def findMedian(self):
        """
        Returns the median of current data stream
        :rtype: float
        """
        if len(self.minHeap) < len(self.maxHeap):
            return -1.0 * self.maxHeap[0]
        else:
            return (self.minHeap[0] - self.maxHeap[0]) / 2.0

# Your MedianFinder object will be instantiated and called as such:
# mf = MedianFinder()
# mf.addNum(1)
# mf.findMedian()

if __name__ == "__main__":
    m = MedianFinder()
    m.addNum(1)
    m.addNum(2)
    print m.findMedian()
    m.addNum(8)
    print m.findMedian()
    m.addNum(10)
    print m.findMedian()
    m.addNum(15)
    print m.findMedian()
    m.addNum(0)
    print m.findMedian()
