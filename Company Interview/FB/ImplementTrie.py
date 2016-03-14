class TrieNode(object):
    def __init__(self):
        self.is_word = False
        self.leaves  = {}

class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root
        for char in word:
            if char not in curr.leaves:
                curr.leaves[char] = TrieNode()
            curr = curr.leaves[char]
        curr.is_word = True

    def search(self, word):
        node = self.find_child_node(word)
        if node is None:
            return False
        return node.is_word

    def startWith(self, prefix):
        return self.find_child_node(prefix) is not None

    def find_child_node(self, word):
        curr = self.root
        for char in word:
            if char in curr.leaves:
                curr = curr.leaves[char]
            else:
                return None
        return curr