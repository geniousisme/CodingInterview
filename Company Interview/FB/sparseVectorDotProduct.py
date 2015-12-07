class Solution(object):
    def vector_product(self, vector1, vector2):
        if len(vector1) != len(vector2):
            return -float("inf")
        return sum([vector1[i] * vector2[i] for i in xrange(len(vector1))])

    def sparse_vector_product(self, vector1, vector2):
        if len(vector1) != len(vector2):
            return -float("inf")
        vect1_dict = {}
        for i in len(vector1):
            if vector1[i] != 0:
                vect1_dict[i] = vector1[i]
        sum = 0
        for idx in vect1_dict:
            if vector2[idx] != 0:
                sum += vector2[idx] * vect1_dict[idx]
        return sum

    def spare_vector_one_pass(self, vector1, vector2):
        if len(vector1) != len(vector2):
            return -float("inf") # which means error
        sum = 0
        for i in xrange(len(vector1)):
            if not (vector1[i] == 0 or vector2[i] == 0):
                sum += vector1[i] * vector2[i]
        return sum

    def sparse_dot_product(x, y): # chen yu's version
        # x and y are in sparse forms
        s = 0
        try:
            x = iter(x)
            y = iter(y)
            xi = next(x)
            yi = next(y)
            while True:
                if xi[0] == yi[0]:
                    s += xi[1] * yi[1]
                    xi = next(x)
                    yi = next(y)
                elif xi[0] > yi[0]:
                    yi = next(y)
                else:
                    xi = next(x)
        except StopIteration:
            return s

    def sparse_vector_dot_product(x, y):
        xi = yi = product = 0
        while xi < len(x) and yi < len(y):
            if x[xi][0] == y[yi][0]:
                product += x[xi][1] * y[yi][1]
                xi += 1; yi += 1 # notice! remember to move on!
            elif x[xi][0] > y[yi][0]:
                yi += 1
            else:
                xi += 1
        return product

x = [(0, 1), (3, 5), (7, 3)]         # [1, 0, 0, 5, 0, 0, 0, 3]
y = [(2, 6), (3, 4), (5, 1), (7, 9)] # [0, 0, 6, 4, 0, 1, 0, 9]
sparse_dot_product(x, y) # 47
sparse_vector_dot_product(x, y)



if __name__ == "__main__":
    s = Solution()
    print s.vector_product([1, 2, 3, 4], [5, 6, 7, 8])
    print s.vector_product([0, 0, 3, 0], [1, 0, 1, 0])
    print s.vector_product([0, 0, 3, 0], [1, 0, 0, 0])

