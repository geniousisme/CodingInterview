class Solution1:
    # @param {integer[][]} matrix
    # @return {integer[]}
    def spiralOrder(self, matrix):
        res = []
        if not matrix: return res
        length = len(matrix[0])
        width  = len(matrix) 
        right = length - 1 
        down  = width  - 1
        left  = up = 0
        count = direction = 0
        while  count < length * width:#length ** 2: # horizontal-dir
               if direction == 0: # 0: right, 1: down, 2: left, 3: up
                  for i in xrange(left, right + 1):
                      res.append(matrix[up][i])
                      count += 1
                  up += 1
               if direction == 1:
                  for i in xrange(up, down + 1):
                      res.append(matrix[i][right])
                      count += 1
                  right -= 1
               if direction == 2:
                  for i in xrange(right, left - 1, -1):
                      res.append(matrix[down][i])
                      count += 1
                  down  -= 1
               if direction == 3:
                  for i in xrange(down, up - 1, -1):
                      res.append(matrix[i][left])
                      count += 1
                  left  += 1
               direction = (direction + 1) % 4
        return res

class Solution(object):
    # @param matrix, a list of lists of integers
    # @return a list of integers
    def spiralOrder(self, matrix):
        result = []
        if matrix == []:
            return result

        left, right, top, bottom = 0, len(matrix[0]) - 1, 0, len(matrix) - 1

        while left <= right and top <= bottom:
            for j in xrange(left, right + 1):
                result.append(matrix[top][j])
            for i in xrange(top + 1, bottom):
                result.append(matrix[i][right])
            for j in reversed(xrange(left, right + 1)):
                if top < bottom:
                    result.append(matrix[bottom][j])
            for i in reversed(xrange(top + 1, bottom)):
                if left < right:
                    result.append(matrix[i][left])
            left, right, top, bottom = left + 1, right - 1, top + 1, bottom - 1

        return result

if __name__ == '__main__':
   s = Solution()
   matrix = [                   \
             [ 1, 2, 3, 4 ],    \
             [ 5, 6, 7, 8 ],    \
             [ 9, 10, 11, 12 ], \
             [ 13, 14, 15, 16 ] \
            ]
   print s.spiralOrder(matrix)
   matrix = [[1,2,3,4,5,6,7,8,9,10]]
   print s.spiralOrder(matrix)