# Given an array of strings, group anagrams together.

# For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"], 
# Return:

# [
#   ["ate", "eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ]
# Note:
# For the return value, each inner list's elements must follow the lexicographic order.
# All inputs will be in lower-case.

class Solution:
    # @param {string[]} strs
    # @return {string[]}
    def __init__(self):
        self.res = []
        self.anagram_dict = {}

    def anagrams(self, strs):
        for string in strs:
            sorted_str = ''.join(sorted(string))
            if not self.anagram_dict.get(sorted_str):
               self.anagram_dict[sorted_str] = [string]
            else:
               self.anagram_dict[sorted_str].append(string)
        for anag_list in self.anagram_dict.values():
            if len(anag_list) > 1:
               self.res.extend(anag_list)
        return self.res

    # def is_anagrams(self, str1, str2):
    #     char_freq_dict = {}
    #     for s in str1:
    #         if not char_freq_dict.get(s):
    #            char_freq_dict[s] = str1.count(s)

if __name__ == '__main__':
   s = Solution()
   strs = ['abc', 'bca', 'cab', 'aa', 'bb', 'cc']
   print s.anagrams(strs)