class Solution:
    # @param A: Given an integer array
    # @return: void
    def left(self, i):
        return 2 * i + 1

    def right(self, i):
        return 2 * i + 2

    def swap(self, A, idx1, idx2):
        A[idx1] = A[idx1] ^ A[idx2]
        A[idx2] = A[idx1] ^ A[idx2]
        A[idx1] = A[idx1] ^ A[idx2]

    def min_heapify(self, A, i, size):
        l = self.left(i)
        r = self.right(i)
        smallest = i # notice: dont use 0 as default!!
        if l < size and A[l] < A[smallest]:
            smallest = l
        if r < size and A[r] < A[smallest]:
            smallest = r
        if smallest != i:
            self.swap(A, smallest, i)
            self.min_heapify(A, smallest, size)

    def heapify(self, A): # build the min heap
        size = len(A)
        for i in xrange(size / 2, -1, -1):
            self.min_heapify(A, i, size)

if __name__ == "__main__":
    s = Solution()
    A =  [45,39,32,11]
    s.heapify(A)
    print A
