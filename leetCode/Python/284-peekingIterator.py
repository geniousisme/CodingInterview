# Time:  O(1) per peek(), next(), hasNext()
# Space: O(1)

# Given an Iterator class interface with methods: next() and hasNext(),
# design and implement a PeekingIterator that support the peek() operation --
# it essentially peek() at the element that will be returned by the next call to next().
#
# Here is an example. Assume that the iterator is initialized to the beginning of
# the list: [1, 2, 3].
#
# Call next() gets you 1, the first element in the list.
#
# Now you call peek() and it returns 2, the next element. Calling next() after that
# still return 2.
#
# You call next() the final time and it returns 3, the last element. Calling hasNext()
# after that should return false.
#

# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator(object):
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """
class PeekingIterator(object):
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iter = iterator
        self.val  = None
        self.has_next = iterator.hasNext()
        self.is_peeked = False

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        if not self.is_peeked:
            self.is_peeked = True
            self.val = self.iter.next()
        return self.val

    def next(self):
        """
        :rtype: int
        """
        self.val = self.peek()
        self.is_peeked = False
        self.has_next = self.iter.hasNext()
        return self.val

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.has_next
