import random

class MineGenerator(object):
    def __init__(self, m, n, k):
        self.width    = m
        self.length   = n
        self.mine_num = k

    def map_generator(self):
        matrix = [[0 for _ in xrange(self.length)] for _ in xrange(self.width)]
        locatons = [(i, j) for j in xrange(self.length) for i in xrange(self.width)]
        for i in xrange(self.mine_num):
            location_idx = random.randint(i, len(locatons) - 1)
            x, y = locatons[location_idx]
            matrix[x][y] = 1
            locatons[location_idx] = locatons[i]
        return matrix

if __name__ == "__main__":
    mg = MineGenerator(3, 4, 5)
    mine_map = mg.map_generator()
    for line in mine_map:
        print line