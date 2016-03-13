#include "include/common.h"

class Solution {
public:
    vector<string> letterCombinations(string digits) {
        vector<string> res;
    }
private:
    string letters[255];
    void init(void) {
         letters['2'] = "abc";
         letters['3'] = "def";
         letters['4'] = "ghi";
         letters['5'] = "jkl";
         letters['6'] = "mno";
         letters['7'] = "pqrs";
         letters['8'] = "tuv";
         letters['9'] = "wxyz";
         return;
    }
    void letter_comb_helper(char number, string digits, int start, string comb, vector<string> res) {
        if (comb.length() == digits.length()) {
            res.push_back(comb);
            return;
        }
        string left = dict[digits[start]];

    }

};

int main(void) {
    Solution s;
    Utils utils;
    utils.printStrVector(s.letterCombinations("23"));
    utils.printStrVector(s.letterCombinations("4"));
    utils.printStrVector(s.letterCombinations("234"));
    return 0;
};