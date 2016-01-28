/*
Given n pairs of parentheses, write a function to generate
all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

"((()))", "(()())", "(())()", "()(())", "()()()"

*/

#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    vector<string> generateParenthesis(int n) {
        vector<string> res;
        if (n > 0)
            parenthesis_generator(n, n, "", res);
        return res;
    }
private:
    void parenthesis_generator(int left, int right, string parent, vector<string>& res) {
        if (left > right)
            return;
        if (left == 0 && right == 0) {
            res.push_back(parent);
            return;
        }
        if (left > 0)
            parenthesis_generator(left - 1, right, parent + "(", res);
        if (right > 0)
            parenthesis_generator(left, right - 1, parent + ")", res);
    }
};

int main(void) {
    Solution s;
    vector<string> res = s.generateParenthesis(3);
    for (auto const &parent: res)
        cout << parent << " ";
    cout << endl;
    return 0;
};