import collections
class WordDistance:
    '''
    Time:  O()
    Space: O()
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



