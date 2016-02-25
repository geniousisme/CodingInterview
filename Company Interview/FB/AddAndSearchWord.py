class TrieNode(object):
    def __init__(self):
        self.leaves = {}
        self.is_word = False

class WordDictionary(object):
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        curr = self.root
        for char in word:
            if char not in curr.leaves:
                curr.leaves[char] = TrieNode()
            curr = curr.leaves[char]
        curr.is_word = True

    def search(self, word):
        return self.search_word_helper(word, 0, self.root)

    def search_word_helper(self, word, start, node):
        if start == len(word):
            return node.is_word
        elif word[start] in node.leaves:
            return self.search_word_helper(word, start + 1, node.leaves[word[start]])
        elif word[start] == '.':
            for char in node.leaves:
                if self.search_word_helper(word, start + 1, node.leaves[char]):
                    return True
        return False
