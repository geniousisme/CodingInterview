class TrieNode(object):
    def __init__(self):
        self.is_string = False
        self.leaves    = {}

class WordDictionary(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.root = TrieNode()

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        curr = self.root
        for char in word:
            if char not in curr.leaves:
                curr.leaves[char] = TrieNode()
            curr = curr.leaves[char]
        curr.is_string = True

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could
        contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        return self.is_searchable(word, 0, self.root)

    def is_searchable(self, word, start, curr):
        if len(word) == start:
            return curr.is_string
        elif word[start] in curr.leaves:
            return self.is_searchable(word, start + 1, curr.leaves[word[start]])
        elif word[start] == '.':
            for char in curr.leaves:
                if self.is_searchable(word, start + 1, curr.leaves[char]):
                    return True
        return False
# Your WordDictionary object will be instantiated and called as such:
# wordDictionary = WordDictionary()
# wordDictionary.addWord("word")
# wordDictionary.search("pattern")