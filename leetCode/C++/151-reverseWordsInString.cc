#include <iostream>
#include <string>
#include <vector>

using namespace std;

class Solution1 {
public:
    void reverseWords(string &s) {
        int start = 0, end = 0;
        while (end < s.length()) {
            if (s[end] != ' ')
                end++;
            else {
                reverse(s, start, end - 1);
                end += 1;
                start = end;
            }
        }
        reverse(s, start, end - 1);
        reverse(s, 0, end - 1);
    }
private:
    void reverse(string &s, int start, int end) {
        while (start < end) {
            char tmp = s[start];
            s[start] = s[end];
            s[end] = tmp;
            start++;
            end--;
        }
    }
};

class Solution {
public:
    void reverseWords(string &s) {
        if (s.empty())
            return;
        string res, word;
        for (int i = s.length() - 1; i >= 0; --i) {
            if (!isspace(s[i]))
                word.push_back(s[i]);
            else {
                if (i < s.length() - 1 && !isspace(s[i + 1])) {
                    reverse(word.begin(), word.end());
                    res.append(word + " ");
                    word.clear();
                }
            }
        }
        if (!isspace(s[0])) {
            reverse(word.begin(), word.end());
            res.append(word);
        }
        else if (!res.empty())
            res.pop_back(); // pop out the last ' '
        s = res;
    }
};

int main(void) {
    Solution s;
    string test1 = "    a    b   ";
    s.reverseWords(test1);
    cout << test1 << endl;
    string test2 = "the sky is blue";
    s.reverseWords(test2);
    cout << test2 << endl;
    return 0;
};