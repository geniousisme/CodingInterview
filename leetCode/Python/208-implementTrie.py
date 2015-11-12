'''
TC: O(N) per action
SC: O(1)
'''

class TrieNode(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.is_string = False
        self.leaves    = {}

class Trie(object):

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        # one character store into leaves of root, one by one
        # if there is no char in the leaves, create one TrieNode for it
        curr = self.root
        for char in word:
            if not char in curr.leaves:
                curr.leaves[char] = TrieNode()
            curr = curr.leaves[char]
        curr.is_string = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        # dfs for the children of the trie,
        # if it can return node, which means we have the word in this trie,
        # but still need to return is_string to check if it is the word
        # ex. if "doggy" in the trie, then when we look for "dog", it will
        # return node, but the node is_string is False.
        # if it return None, then which means there is no such word.
        node = self.childSearch(word)
        if node:
            return node.is_string
        return False

    def childSearch(self, word):
        # look for the children node for word
        curr = self.root
        for char in word:
            if char in curr.leaves:
                curr = curr.leaves[char]
            else:
                return None
        return curr


    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie
        that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        # since we only need to check the prefix,
        # then it can just be judged by checking if it is node or not.
        return self.childSearch(prefix) is not None
