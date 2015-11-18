class Solution1(object): # iterative
    def __init__(self):
        self.digit_letter_dict = \
                                {
                                '0':[""],
                                '1':[""],
                                '2':['a', 'b', 'c'],
                                '3':['d', 'e', 'f'],
                                '4':['g', 'h', 'i'],
                                '5':['j', 'k', 'l'],
                                '6':['m', 'n', 'o'],
                                '7':['p', 'q', 'r', 's'],
                                '8':['t', 'u', 'v'],
                                '9':['w', 'x', 'y', 'z']
                                }

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        letter_combs = []
        for digit in digits:
            letter_combs = self.merge_letter_combs(self.digit_letter_dict[digit], letter_combs)
        return letter_combs

    def merge_letter_combs(self, letters, letter_combs):
        if not letter_combs:
            return letters
        comb_list = []
        for letter in letters:
            comb_list.extend(letter_comb + letter for letter_comb in letter_combs)
        return comb_list


if __name__ == "__main__":
    s = Solution()
    print s.letterCombinations("234")
