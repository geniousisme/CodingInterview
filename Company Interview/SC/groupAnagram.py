from collections import defaultdict
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagram_dict = defaultdict(list)
        for string in strs:
            sorted_str = ''.join(sorted(string))
            anagram_dict[sorted_str].append(string)
        result = []
        for word_list in anagram_dict.values():
            word_list.sort()
            result.append(word_list)
        return result

if __name__ == "__main__":
    s = Solution()
    print s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])


        