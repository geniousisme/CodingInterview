/*
    Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

    If the last word does not exist, return 0.

    Note: A word is defined as a character sequence consists of non-space characters only.

    For example,
    Given s = "Hello World",
    return 5.
*/

#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int lengthOfLastWord(string s) {
        /*
            Time:   O(n)
            Space:  O(1)
        */
        int s_len = s.length();
        if (s_len == 0)
            return 0;
        int last_word_len = 0;
        for (int i = s_len - 1; i >= 0; --i) {
            if (s[i] != ' ')
                last_word_len++;
            else {
                if (last_word_len > 0)
                    return last_word_len;
            }
        }
        return last_word_len;
    }
};

int main(void) {

    Solution s;
    cout << s.lengthOfLastWord("Hello World") << endl;
    cout << s.lengthOfLastWord("Hello man!") << endl;
    cout << s.lengthOfLastWord("Hello you are such a bitch!") << endl;

    return 0;
}