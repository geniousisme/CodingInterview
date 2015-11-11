# Time:  O(m * n * l)
# Space: O(l)
#
# Given a 2D board and a word, find if the word exists in the grid.
#
# The word can be constructed from letters of sequentially adjacent cell, 
# where "adjacent" cells are those horizontally or vertically neighboring. 
# The same letter cell may not be used more than once.
#
# For example,
# Given board =
#
# [
#   "ABCE",
#   "SFCS",
#   "ADEE"
# ]
# word = "ABCCED", -> returns true,
# word = "SEE", -> returns true,
# word = "ABCB", -> returns false.
#

class Solution:
    # @param board, a list of lists of 1 length string
    # @param word, a string
    # @return a boolean
    def exist(self, board, word):
        visited = [[False for j in xrange(len(board[0]))] for i in xrange(len(board))]

        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                if self.existRecu(board, word, 0, i, j, visited):
                    return True

        return False

    def existRecu(self, board, word, cur, i, j, visited):
        if cur == len(word):
            return True

        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or visited[i][j] or board[i][j] != word[cur]:
            return False

        visited[i][j] = True
        result = self.existRecu(board, word, cur + 1, i + 1, j, visited) or\
                 self.existRecu(board, word, cur + 1, i - 1, j, visited) or\
                 self.existRecu(board, word, cur + 1, i, j + 1, visited) or\
                 self.existRecu(board, word, cur + 1, i, j - 1, visited)         
        visited[i][j] = False

        return result

class Solution1:
    # @param board, a list of lists of 1 length string
    # @param word, a string
    # @return a boolean
    def exist(self, board, word):
        solution = False
        for i in range(0,len(board)):
            for j in range(0, len(board[0])):
                solution = solution or self.existRec(board, word, i, j, 0)
        return solution

    def existRec(self, board, word, row, col, index):
        if row < 0 or row>=len(board) or col<0 or col>=len(board[0]) or  board[row][col]!=word[index]:
            return False
        if index==len(word)-1:
            return True
        board[row][col] = "$"
        solution = self.existRec(board, word, row-1, col, index+1) or self.existRec(board, word, row+1, col, index+1) or self.existRec(board, word, row, col-1, index+1) or self.existRec(board, word, row, col+1, index+1)
        board[row][col] = word[index]
        return solution

# Chris:TODO:: rewrite the iterative version

class Solution2:
    # @param board, a list of lists of 1 length string
    # @param word, a string
    # @return a boolean
    def exist(self, board, word):
        def dfs(x, y, word):
            if len(word)==0: return True
            #up
            if x>0 and board[x-1][y]==word[0]:
                tmp=board[x][y]; board[x][y]='#'
                if dfs(x-1,y,word[1:]):
                    return True
                board[x][y]=tmp
            #down
            if x<len(board)-1 and board[x+1][y]==word[0]:
                tmp=board[x][y]; board[x][y]='#'
                if dfs(x+1,y,word[1:]):
                    return True
                board[x][y]=tmp
            #left
            if y>0 and board[x][y-1]==word[0]:
                tmp=board[x][y]; board[x][y]='#'
                if dfs(x,y-1,word[1:]):
                    return True
                board[x][y]=tmp
            #right
            if y<len(board[0])-1 and board[x][y+1]==word[0]:
                tmp=board[x][y]; board[x][y]='#'
                if dfs(x,y+1,word[1:]):
                    return True
                board[x][y]=tmp
            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]==word[0]:
                    if(dfs(i,j,word[1:])):
                        return True
        return False


if __name__ == '__main__':
   s = Solution()
   board =  [          \
              ["ABCE"],\
              ["SFCS"],\
              ["ADEE"] \
            ]
   # print s.exist(board, "ABCCED")
   # print s.exist(board, "SEE")
   print s.exist(board, "ABCB")

