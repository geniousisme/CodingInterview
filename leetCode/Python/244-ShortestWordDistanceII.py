# This is a follow up of Shortest Word Distance.
# The only difference is now you are given the list of words
# and your method will be called repeatedly many times with different parameters.
# How would you optimize it?

# Design a class which receives a list of words in the constructor,
# and implements a method that takes two words word1 and word2
# and return the shortest distance between these two words in the list.

# For example,
# Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

# Given word1 = “coding”, word2 = “practice”, return 3.
# Given word1 = "makes", word2 = "coding", return 1.

# Note:
# You may assume that word1 does not equal to word2,
# and word1 and word2 are both in the list.

import collections
class WordDistance:
    '''
    Time:  O(a + b)
    Space: O(n)
    '''
    def __init__(self, words):
        self.word_idx_dict = collections.defaultdict(list)
        for i in xrange(len(words)):
            self.word_idx_dict[words[i]].append(i)

    def shortest(self, word1, word2):
        idx1_list = self.word_idx_dict[word1]
        idx2_list = self.word_idx_dict[word2]
        i = j = 0
        shortest_idst = float("inf")
        while i < len(idx1_list) and j < len(idx2_list):
            shortest_idst = min(abs(idx1_list[i] - idx2_list[j]), shortest_idst)
            if idx1_list[i] > idx2_list[j]:
                j += 1
            else:
                i += 1
        return shortest_idst

if __name__ == "__main__":
    w = WordDistance(["practice", "makes", "perfect", "coding", "makes"])
    print w.shortest("coding", "makes")
    print w.shortest("practice", "coding")



