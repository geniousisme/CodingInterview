import heapq
import random

class TopkHeap(object):
    def __init__(self, k):
        self.k = k
        self.data = []

    def Push(self, elem):
        if len(self.data) < self.k:
            heapq.heappush(self.data, elem)
        else:
            topk_small = self.data[0]
            if elem > topk_small:
                heapq.heapreplace(self.data, elem)

    def TopK(self):
        # return [x for x in [heapq.heappop(self.data) for x in xrange(len(self.data))]]
        return [heapq.heappop(self.data) for x in xrange(self.k)]


class TopKDictHeap(object):
      def __init__(self, k):
          self.dict  = {}
          self.words = []
          self.k     = k

      def push(self, word):
          if len(self.words) < self.k:
             heapq.heappush(self.words, (self.dict[word], word))
             # print self.words
          else:
             topk_smallest = self.words[0][1]
             # print topk_smallest
             if self.dict[word] > self.dict[topk_smallest]:
                heapq.heapreplace(self.words, (self.dict[word], word))
             elif self.dict[word] == self.dict[topk_smallest] and word > topk_smallest:
                  heapq.heapreplace(self.words, (self.dict[word], word))

      def TopK(self):
          return [heapq.heappop(self.words) for i in xrange(len(self.words))]


if __name__ == "__main__":
    list_rand = random.sample(xrange(1000000), 100)
    # th = TopkHeap(3)
    # for i in list_rand:
    #     th.Push(i)
    # print th.TopK()
    # print sorted(list_rand, reverse=True)[0:3]
    words = ["la", "la", "la", "hey", "hey", "a", "a", "b", "c", "d"]
    tdh   = TopKDictHeap(3)
    for word in words:
        tdh.dict[word] = tdh.dict.get(word, 0) + 1
    # print tdh.dict
    for key in tdh.dict.keys():
        tdh.push(key)
    print tdh.TopK()
    dict  = {}
    for word in words:
        dict[word] = dict.get(word, 0) + 1
    print dict
    print heapq.nlargest(3, dict, key=dict.get)
    