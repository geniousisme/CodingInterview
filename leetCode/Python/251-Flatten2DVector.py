# Implement an iterator to flatten a 2d vector.

# For example,
# Given 2d vector =
# [
#   [1,2],
#   [3],
#   [4,5,6]
# ]

# By calling next repeatedly until hasNext returns false,
# the order of elements returned by next should be: [1, 2, 3, 4, 5, 6].

class Vector2D(object):
    # Initialize your data structure here.
    # @param {integer[][]} vec2d
    def __init__(self, vec2d):
        self.vec = vec2d
        self.x = 0
        self.y = 0
        self.adjust_next_iter()

    # @return {integer}
    def next(self):
        ret = -1
        # check if it has next first
        if self.hasNext():
            # current element
            ret = self.vec[self.x][self.y]
            # move horizontally to look for the next element
            self.y += 1
            # check if it reach the end of the vector
            self.adjust_next_iter()
        return ret

    # @return {boolean}
    def hasNext(self):
        return self.x < len(self.vec) and self.y < len(self.vec[self.x])

    def adjust_next_iter(self):
        # use while to skip the empty vector, see the third test case
        while self.x < len(self.vec) and self.y >= len(self.vec[self.x]):
            # if it reach the end of the vector, then move the next row
            self.x += 1
            # and set the col to zero to start from the beginning.
            if self.x < len(self.vec):
                self.y = 0

if __name__ == "__main__":
    vec2d = Vector2D([[1, 2, 3], [4, 5], [6, 7]])
    print vec2d.next()
    print vec2d.next()
    print vec2d.next()
    print vec2d.next()
    print vec2d.next()
    print vec2d.next()
    print vec2d.next()
    print vec2d.next()
    vec2d = Vector2D([[], [1, 2], [3], [], [5, 6]]) # third test case
    print vec2d.next()
    print vec2d.next()
    print vec2d.next()
    print vec2d.next()
    print vec2d.next()
    print vec2d.next()
    print vec2d.next()
