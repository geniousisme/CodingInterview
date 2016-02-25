def longest_chain(dictionary):

    class Solution(object):
        def __init__(self):
            self.longest_len = 0
            self.word_list = []
            self.dict = {}

        def longest_chain(self, dictionary):
            if self.longest_len:
                self.longest_len = 0
            # self.word_list = sorted(list(set(dictionary)), key=len, reverse=True)
            self.word_list = dictionary

            for i in xrange(len(self.word_list)):
                self.dict[self.word_list[i]] = i
            for word in self.word_list:
                self.longest_chain_helper(word, 0)
            return self.longest_len

        def longest_chain_helper(self, word, curr_len):
            if self.dict.get(word) is None:
                self.longest_len = max(curr_len, self.longest_len)
                return
            for i in xrange(len(word)):
                self.longest_chain_helper(word[:i] + word[i + 1:], curr_len + 1)

    s = Solution()
    return s.longest_chain(dictionary)

if __name__ == "__main__":
    # s = Solution()
    dict1 = ["abcd", "bcd", "bd", "defgh", "cd", "d"]
    print longest_chain(dict1)
    dict2 = ["a", "bcd", "abd", "cd", "c", "c"]
    print longest_chain(dict2)


