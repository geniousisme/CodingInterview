def print_diagonally(matrix):
    res = []
    row = 0
    # i, j
    queue = []

    while queue or row < len(matrix):
        for _ in xrange(len(queue)):
            i, j = queue.pop(0)
            if j < len(matrix[i]):
                res.append(matrix[i][j])
                queue.append((i, j+1))
        if row < len(matrix):
            queue.append((row, 0))
            row += 1
    return res

print print_diagonally([])
print print_diagonally([[1,2,4,7], [3,5,8], [6,9], [10]])
print print_diagonally([[1,2], [3,4,6,8], [5], [7,9,11], [10]])
print print_diagonally([[], [1,2], [3,4,6,8], [5], [7,9,11], [10]])
