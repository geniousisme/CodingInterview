# An abbreviation of a word follows the form <first letter><number><last letter>. Below are some examples of word abbreviations:

# a) it                      --> it    (no abbreviation)

#      1
# b) d|o|g                   --> d1g

#               1    1  1
#      1---5----0----5--8
# c) i|nternationalizatio|n  --> i18n

#               1
#      1---5----0
# d) l|ocalizatio|n          --> l10n
# Assume you have a dictionary and given a word, find whether its abbreviation is unique in the dictionary. A word's abbreviation is unique if no other word from the dictionary has the same abbreviation.

# Example:
# Given dictionary = [ "deer", "door", "cake", "card" ]

# isUnique("dear") -> false
# isUnique("cart") -> true
# isUnique("cane") -> false
# isUnique("make") -> true

# Time:  ctor:   O(n), n is number of words in the dictionary.
#        lookup: O(1)
# Space: O(k), k is number of unique words.

import collections

class ValidWordAbbr(object):
    def __init__(self, dictionary):
        if dictionary:
            self.dict = collections.defaultdict(list)
            for word in dictionary:
                if len(word)
                self.dict[word[0] + str(len(word) - 2) + word[-1]].append(word)

    def isUnique(self, word):
        if len(word) >= 2:
            key = word[0] + str(len(word) - 2) + word[-1]
            if key not in self.dict:
                return True
            elif len(self.dict[key]) == 1 and self.dict[key][0] == word:
                return True
            else:
                return False

if __name__ == "__main__":
    v = ValidWordAbbr(["deer", "door", "cake", "card"])
    print v.isUnique("dear")
    print v.isUnique("cart")
    print v.isUnique("cane")
    print v.isUnique("make")
