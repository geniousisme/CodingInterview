class Solution(object):
    def wordPattern(self, pattern, string):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        word_list = string.split()
        if len(word_list) != len(pattern):
            return False
        pattern_char_word_dict = {}
        word_pattern_char_dict = {}
        for idx, pattern_char in enumerate(pattern):
            if not pattern_char_word_dict.get(pattern_char):
                pattern_char_word_dict[pattern_char] = word_list[idx]
            if not word_pattern_char_dict.get(word_list[idx]):
                word_pattern_char_dict[word_list[idx]] = pattern_char
            if (pattern_char_word_dict.get(pattern_char) != word_list[idx] or 
                    word_pattern_char_dict.get(word_list[idx]) != pattern_char):
                return False
        return True
            