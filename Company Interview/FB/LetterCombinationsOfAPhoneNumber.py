class Solution1(object):
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
    def letterCombinations(self, digits): # recursive way
        def letter_comb_helper(comb, start):
            if len(comb) == len(digits):
                res.append(comb)
                return
            for letter in self.digit_letter_dict[digits[start]]:
                letter_comb_helper(comb + letter, start + 1)
        res = []
        if digits:
            letter_comb_helper("", 0)
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
    def letterCombinations(self, digits): # iterative way
        letter_comb_list = []
        if digits:
            for digit in digits:
                letter_comb_list = self.merge_comb_list(letter_comb_list, self.digit_letter_dict[digit])
        return letter_comb_list

    def merge_comb_list(self, letter_comb_list, letters):
        if not letter_comb_list:
            return letters
        tmp_comb_list = []
        for letter in letters:
            tmp_comb_list += [letter_comb + letter for letter_comb in letter_comb_list]
        return tmp_comb_list

if __name__ == "__main__":
    s = Solution()
    print s.letterCombinations("23")

