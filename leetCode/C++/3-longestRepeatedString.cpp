#include <iostream>
#include <string>
#include <unordered_map>
#include <vector>

using namespace std;

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int end = 1, start = 0, longest_length = 0;
        string tmp;
        for (end = 1; end < s.length(); end++) {
            tmp = tmp.assign(s, start, end);
            if (tmp.find(s[end]) == npos) {
                longest_length = max(end - start, longest_length);
            } else {
                start += tmp.find(s, start, end) + 1;
            }
        }
        // if (longest_length == 0)
        //     longest_length = end - start + 1;
        return longest_length;
    }
};

int main(void) {
    Solution s;
    cout << s.lengthOfLongestSubstring("abcabcbb") << endl;
    cout << s.lengthOfLongestSubstring("abcbbbbeftgvdssbb") << endl;
    cout << s.lengthOfLongestSubstring("bbbb") << endl;
    cout << s.lengthOfLongestSubstring("b") << endl;
    cout << s.lengthOfLongestSubstring("adfewqbclo") << endl;
    cout << s.lengthOfLongestSubstring("aab") << endl;


    return 0;
}