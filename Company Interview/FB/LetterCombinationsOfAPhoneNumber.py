class Solution(object):
    '''
    Time:  O(n * 4 ^ n)
    Space: O(n)
    '''
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
        def letter_comb_helper(start, comb):
            if len(comb) == length:
                res.append(comb)
                return
            for letter in self.digit_letter_dict[digits[start]]:
                letter_comb_helper(start + 1, comb + letter)
        res = []; length = len(digits)
        if digits:
            letter_comb_helper(0, "")
        return res

class Solution(object):
    '''
    Time:  O(n * 4 ^ n)
    Space: O(n)
    '''
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
        res = []
        if digits:
            for digit in digits:
                res = self.merge_comb_list(res, self.digit_letter_dict[digit])
        return res

    def merge_comb_list(self, letter_combs, letters):
        if not letter_combs:
            return letters
        comb_list = []
        for letter in letters:
            comb_list.extend([letter_comb + letter for letter_comb in letter_combs])
        return comb_list
