class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        str_hash, ptn_hash = {}, {}
        str_list = str.split()
        if len(str_list) != len(pattern):
            return False
        for ptn, str in zip(pattern, str_list):
            if str_hash.get(ptn) is None:
                str_hash[ptn] = str
            if ptn_hash.get(str) is None:
                ptn_hash[str] = ptn
            if str != str_hash[ptn] or ptn_hash[str] != ptn:
                    return False
        return True

if __name__ == "__main__":
    s = Solution()
    print s.wordPattern("abba", "dog cat cat dog")
    print s.wordPattern("abba", "dog cat cat fish")
    print s.wordPattern("abba", "dog dog dog dog")

