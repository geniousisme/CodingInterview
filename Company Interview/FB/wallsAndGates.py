class Solution(object):
    def wallsAndGates(self, rooms):
        INF = 2 ^ 31 - 1
        # since we only need to iterate the surrounding elements of gates first, store the gates cord into queue
        queue = [(i, j) for j in xrange(len(rooms[0])) for i in xrange(len(rooms)) if rooms[i][j] == 'G']
        while queue:
            (i, j) = queue.pop(0)
            # iterate the four surrounding elements
            for I, J in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if -1 < I < len(rooms) and -1 < J < len(rooms[0]) and rooms[I][J] == '_':
                    # if it is gates, make current element to be 1
                    if rooms[i][j] == 'G':
                        rooms[I][J] = '1'
                    # if it is not gates, which means it is the _ which already had distance
                    else:
                        rooms[I][J] = str(int(rooms[i][j]) + 1)
                    # store the cord to make its surrounding element be able to count the distance
                    queue.append((I, J))

if __name__ == "__main__":
    s = Solution()
    rooms = [['_', 'W', 'G', '_'], ['_', '_', '_', 'W'], ['_', 'W', '_', 'W'], ['G', 'W', '_', '_']]
    s.wallsAndGates(rooms)
    for room in rooms:
        print room