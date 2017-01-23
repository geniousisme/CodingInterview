'''
Given an array of words and a length L, format the text such that each line has exactly L characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly L characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line do not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left justified and no extra space is inserted between words.

For example,
words: ["This", "is", "an", "example", "of", "text", "justification."]
L: 16.


"This    is    an",
"example  of text",
"justification.  "
'''
from math import ceil

class Solution(object):
    def justify(self, words, len_limit):
        line_len = 0
        line = []
        while words:
            # print words
            word = words.pop(0)
            if (line_len + len(word) == len_limit or 
                line_len + len(word) + 1 == len_limit):
                line.append(word)
                line_len += len(word)
                result = self.justifier(line, len_limit - (line_len - len(line) + 1))
                print result
                line = []
                line_len = 0
            elif line_len + len(word) > len_limit:
                result = self.justifier(line, len_limit - (line_len - len(line)))
                print result
                line = []
                line_len = 0
                words.insert(0, word)
            else:
                line.append(word)
                line_len += len(word) + 1
        print self.justifier(line, len_limit - (line_len - len(line)))

    def justifier(self, line, left_space_num):
        if len(line) == 1:
            return line[0] + ' ' * left_space_num
        if left_space_num % (len(line) - 1) == 0:
            space_num = left_space_num / (len(line) - 1)
            return (' ' * space_num).join(line)
        else:
            result = ""
            interval_num = len(line) - 1
            idx = 0
            while left_space_num:
                space_num = ceil(left_space_num * 1.0 / interval_num)
                left_space_num -= space_num
                interval_num -= 1
                result += line[idx] + ' ' * int(space_num)
                idx += 1
            result += line[idx]
            return result

if __name__ == "__main__":
    s = Solution()
    print s.justifier(["This", "is", "an"], 8)
    print s.justifier(["example", "of", "text"], 3)
    print s.justifier(["justification."], 3)
    words = ["This", "is", "an", "example", "of", "text", "justification."]
    L = 16
    s.justify(words, L)