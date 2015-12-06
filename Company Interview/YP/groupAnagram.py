class Solution(object):
    def groupAnagrams(self, strs):
        """
        Time:  O(26 * m * n) => O(mn)
        Space: O(n)
        """
        word_hash = {}
        strs.sort()
        for string in strs:
            # sorted_str = ''.join(sorted(string))
            sorted_str = self.get_sorted_str(string)
            if sorted_str in word_hash:
                word_hash[sorted_str].append(string)
            else:
                word_hash[sorted_str] = [string]
        return word_hash.values()

    def get_sorted_str(self, str):
        sorted_str = ""
        count_char = [0] * 26
        for char in str:
            count_char[ord(char) - ord('a')] += 1
        for i in xrange(26):
            while count_char[i] != 0:
                sorted_str += chr(i + ord('a'))
                count_char[i] -= 1
        return sorted_str

if __name__ == "__main__":
    s = Solution()
    strs = ['rat', 'art', 'tar', 'bats', 'abts', 'sabt', 'banana']
    print s.groupAnagrams(strs)
