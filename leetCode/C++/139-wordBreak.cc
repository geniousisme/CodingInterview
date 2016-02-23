/*

Given a string s and a dictionary of words dict,
determine if s can be segmented into a space-separated sequence of one or more dictionary words.

For example, given
s = "leetcode",
dict = ["leet", "code"].

Return true because "leetcode" can be segmented as "leet code".

Subscribe to see which companies asked this question

*/

#include <iostream>
#include <unordered_set>
#include <vector>

using namespace std;

class Solution {
public:
    bool wordBreak(string s, unordered_set<string>& wordDict) {
        /*
            Time:  O(n ^ 2)
            Space: O(n)
        */
        vector<bool> dp(s.length() + 1, false);
        dp[0] = true;
        for (int i = 1; i <= s.length(); ++i) {
            for (int j = 0; j < i; ++j) {
                if (dp[j] && wordDict.find(s.substr(j, i - j)) != wordDict.end())
                    dp[i] = true;
            }
        }
        return dp[s.length()];
    }
};

int main(void) {
  Solution s;
  string test = "leetcode";
  unordered_set<string> dict = { "leetcode" };
  cout << s.wordBreak(test, dict) << endl;
  string test1 = "ab";
  unordered_set<string> dict1 = { "a", "b" };
  cout << s.wordBreak(test1, dict1) << endl;
  string test2 = "a";
  unordered_set<string> dict2 = { "a"};
  cout << s.wordBreak(test2, dict2) << endl;
  return 0;
};