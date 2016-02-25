# This is a follow up of Shortest Word Distance.
# The only difference is now word1 could be the same as word2.
# Given a list of words and two words word1 and word2,
# return the shortest distance between these two words in the list.
# word1 and word2 may be the same and they represent two individual words in the list.

class Solution:
    # @param {string[]} words
    # @param {string} word1
    # @param {string} word2
    # @return {integer}
    def shortestWordDistance(self, words, word1, word2):
        '''
        Time:  O(n)
        Space: O(1)
        '''
        shortest_dist = float("inf")
        i = 0; idx1 = None; idx2 = None
        while i < len(words):
            if words[i] == word1:
                if idx1 is not None:
                    shortest_dist = min(abs(idx1 - i), shortest_dist)
                idx1 = i
            elif words[i] == word2:
                idx2 = i
            if idx1 is not None and idx2 is not None:
                shortest_dist = min(abs(idx1 - idx2), shortest_dist)
            i += 1
        return shortest_dist

if __name__ == "__main__":
    s = Solution()
    print s.shortestWordDistance(["practice", "makes", "perfect", "coding", "makes"], "makes", "coding")
    print s.shortestWordDistance(["practice", "makes", "perfect", "coding", "makes"], "makes", "makes")
