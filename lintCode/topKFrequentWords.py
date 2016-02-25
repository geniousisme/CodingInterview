class Solution:
    # @param {string[]} words a list of string
    # @param {int} k an integer
    # @return {string[]} a list of string
    def __init__(self):
        self.word_counts = {}
    def topKFrequentWords(self, words, k):
        # Write your code here
        for word in words:
            if self.word_counts.get(word, 0) != 0:
                self.word_counts[word] += 1
            else:
                self.word_counts[word] = 1
        words = sorted(self.word_counts.keys(), cmp=self.comparator)
        return words[:k]

    def comparator(self, word1, word2):
        # make it reverse directly at first place.
        if self.word_counts[word1] > self.word_counts[word2]:
            return -1
        elif self.word_counts[word1] == self.word_counts[word2] and word1 < word2:
            return -1
        elif self.word_counts[word1] == self.word_counts[word2] and word1 == word2:
            return 0
        else:
            return 1

if __name__ == "__main__":
     s = Solution()
     words = [                              \
                "yes", "lint", "code",      \
                "yes", "code", "baby",      \
                "you", "baby", "chrome",    \
                "safari", "lint", "code",   \
                "body", "lint", "code"      \
             ]
     print s.topKFrequentWords(words, 3)
     print s.topKFrequentWords(words, 4)
