from collections import defaultdict

class Solution(object):
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        hash_str_word_list_dict = defaultdict(list)
        for string in strings:
            hash_str_word_list_dict[self.hash_str(string)].append(string)

        result = []
        for string_list in hash_str_word_list_dict.values():
            result.append(sorted(string_list))

        return result
            
    def hash_str(self, s):
        base = ord(s[0])
        hash_str = ""
        for i in xrange(len(s)):
            if ord(s[i]) - base >= 0:
                hash_str += unichr(ord('a') + ord(s[i]) - base)
            else:
                hash_str += unichr(ord('a') + ord(s[i]) - base + 26)
        return hash_str
