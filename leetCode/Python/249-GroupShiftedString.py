# Given a string, we can "shift" each of its letter to its successive letter,
# for example: "abc" -> "bcd". We can keep "shifting" which forms the sequence:

# "abc" -> "bcd" -> ... -> "xyz"
# Given a list of strings which contains only lowercase alphabets,
# group all strings that belong to the same shifting sequence.

# For example, given: ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"],
# Return:

# [
#   ["abc","bcd","xyz"],
#   ["az","ba"],
#   ["acef"],
#   ["a","z"]
# ]
# Note: For the return value, each inner list's elements must follow the lexicographic order.
from collections import defaultdict

class Solution:
    '''
    Time:  O(nlogn)
    Space: O(n)
    '''
    def groupStrings(self, strings):
        groups = defaultdict(list)
        for string in strings:
            groups[self.shift(string)].append(string)
        return map(sorted, groups.values())

    def shift(self, string):
        return tuple([(ord(char) - ord(string[0])) % 26 for char in string])

if __name__ == "__main__":
    s = Solution()
    print s.groupStrings(["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"])