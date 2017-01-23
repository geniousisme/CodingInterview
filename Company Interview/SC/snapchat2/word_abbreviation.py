class TrieNode(object):
    def __init__(self):
        self.unique = True
        self.children = {}


class TrieTree(object):
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        p = self.root
        for w in word:
            if w not in p.children:
                p.children[w] = TrieNode()
            else:
                p.children[w].unique = False
            p = p.children[w]


def abbrev(words):
    trees = {}
    for word in words:
        key = word[0] + str(len(word)) + word[-1]
        if key not in trees:
            trees[key] = TrieTree()
        trees[key].insert(word)

    result = []
    for word in words:
        root = trees[word[0] + str(len(word)) + word[-1]].root
        for i, ch in enumerate(word):
            root = root.children[ch]
            if root.unique:
                # compress and add
                compressed = word[:i+1] + str(len(word)) + word[-1]
                if len(compressed) >= len(word):
                    result.append(word)
                else:
                    result.append(compressed)
                break
    return result



expected = ['l4e', 'god', 'internal', 'me', 'i8t', 'interval', 'inte9n', 'f4j', 'intr9n']
result = abbrev(['like', 'god',  'internal', 'me', 'internet', 'interval', 'intension', 'fthj', 'intrusion'])
print result
assert(expected == result)
