# Time:  O(n)
# Space: O(n)
#
# All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T, 
# for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.
# 
# Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.
#
# For example,
#
# Given s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT",
#
# Return:
# ["AAAAACCCCC", "CCCCCAAAAA"].
#

class Solution:
    # @param s, a string
    # @return a list of strings
    def findRepeatedDnaSequences(self, s):
        dictionary = {'A' : 0, 'C': 1, 'G' : 2, 'T' : 3}
        res = []
        sum = 0
        seq_val_freq = {}
        for i in xrange(len(s)):
            sum = (sum * 4 + dictionary[s[i]]) & 0xFFFFF
            if i < 9:
               continue
            seq_val_freq[sum] = seq_val_freq.get(sum, 0) + 1
            if seq_val_freq[sum] == 2:
               res.append(s[i - 9:i + 1])
        return res

class Solution2:
    def findRepeatedDnaSequences(self, s): # pure dict version
        dic = {}
        for i in xrange(len(s) - 9):
            dic[s[i:i+10]] = dic.get(s[i:i+10], 0) + 1
        return [res for res in dic.keys() if dic[res] > 1]

if __name__ == '__main__':
   s = Solution()
   print s.findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT")