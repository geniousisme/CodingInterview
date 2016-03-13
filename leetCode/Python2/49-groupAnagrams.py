class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        word_hash = {}
        strs.sort()
        for string in strs:
            sorted_str = ''.join(sorted(string))
            if sorted_str in word_hash:
                word_hash[sorted_str].append(string)
            else:
                word_hash[sorted_str] = [string]
        return [val for val in word_hash.values()]

if __name__ == "__main__":
    s = Solution()
    print s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])