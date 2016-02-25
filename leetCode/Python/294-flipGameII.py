# You are playing the following Flip Game with your friend:
# Given a string that contains only these two characters: + and -,
# you and your friend take turns to flip two consecutive "++" into "--".
# The game ends when a person can no longer make a move and
# therefore the other person will be the winner.

# Write a function to determine if the starting player can guarantee a win.
# For example, given s = "++++", return true.
# The starting player can guarantee a win by flipping the middle "++" to become "+--+".

# Follow up:
# Derive your algorithm's runtime complexity.

class Solution(object):
    def canWin(self, s):
        i = 0; n = len(s) - 1; is_win = False
        while not is_win and i < n:
            if s[i] == '+':
                while not is_win and i < n and s[i + 1] == '+':
                    is_win = not self.canWin(s[:i] + "--" + s[i + 2:])
                    i += 1
            i += 1
        return is_win
