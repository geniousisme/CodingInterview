/*

Given a string containing just the characters
'(', ')', '{', '}', '[' and ']', determine if the input string is valid.
The brackets must close in the correct order,
"()" and "()[]{}" are all valid but "(]" and "([)]" are not.

*/

#include <iostream>
#include <stack>
#include <vector>

using namespace std;

class Solution {
public:
    bool isValid(string s) {
        stack<char> stk;
        for (const auto &c: s) {
            if (c == '[' || c == '(' || c == '{')
                stk.push(c);
            else {
                if (c == ']') {
                    if (!stk.empty() && stk.top() == '[')
                        stk.pop();
                    else
                        return false;
                }
                if (c == ')') {
                    if (!stk.empty() && stk.top() == '(')
                        stk.pop();
                    else
                        return false;
                }
                if (c == '}') {
                    if (!stk.empty() && stk.top() == '{')
                        stk.pop();
                    else
                        return false;
                }
            }
        }
        return stk.empty();
    }
};

int main(void) {
    Solution s;
    cout << s.isValid("()[]{}") << endl;
    cout << s.isValid("([)]") << endl;
    cout << s.isValid(")") << endl;
    cout << s.isValid(")}{({))[{{[}") << endl;

    return 0;
};