/*
Write a function to find the longest
common prefix string amongst an array of strings.
*/

#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        string common_prefix = "";
        if (!strs.empty()) {
            for (int i = 0; i < strs[0].length(); ++i) {
                for (int j = 1; j < strs.size(); ++j) {
                    if (i > strs[j].length() || strs[0][i] != strs[j][i])
                        return common_prefix;
                }
                common_prefix += strs[0][i];
            }
        }
        return common_prefix;
    }
};

int main(void) {
    Solution s;
    vector<string> strs {"abc", "abcd", "ab"};
    cout << s.longestCommonPrefix(strs) << endl;
    return 0;
}