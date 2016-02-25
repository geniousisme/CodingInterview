# Given a list of words and two words word1 and word2,
# return the shortest distance between these two words in the list.

# For example,
# Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

# Given word1 = "coding", word2 = "practice", return 3.
# Given word1 = "makes", word2 = "coding", return 1.

# Note:
# You may assume that word1 does not equal to word2,
# and word1 and word2 are both in the list.
class Solution:
    # @param {string[]} words
    # @param {string} word1
    # @param {string} word2
    # @return {integer}
    def shortestDistance(self, words, word1, word2):
        '''
        Time:  O(n)
        Space: O(1)
        '''
        idx1 = idx2 = None
        shortest_dist = float("inf")
        for i in xrange(len(words)):
            if word1 == words[i]:
                idx1 = i
            elif word2 == words[i]:
                idx2 = i
            if idx1 is not None and idx2 is not None and abs(idx2 - idx1) < shortest_dist:
                shortest_dist = abs(idx2 - idx1)
        return shortest_dist

if __name__ == "__main__":
    s = Solution()
    print s.shortestDistance(["practice", "makes", "perfect", "coding", "makes"], "makes", "coding")
    print s.shortestDistance(["practice", "makes", "perfect", "coding", "makes"], "coding", "practice")
