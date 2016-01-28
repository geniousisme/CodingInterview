/*

Given a roman numeral, convert it to an integer.
Input is guaranteed to be within the range from 1 to 3999.

*/

#include <iostream>

class Solution {
public:
    int romanToInt(string s) {
        /*
            Time:  O(n)
            Space: O(1)
        */
        int res = 0;
        init();
        for (int i = 0; i < s.length(); ++i) {
             if (romanTable[s[i + 1]] > romanTable[s[i]])
                 res -= romanTable[s[i]];
             else
                 res += romanTable[s[i]];
        };
        return res;
    }
private:
    // really fast way to use initialize table.
    int romanTable[255];
    void init(void) {
         romanTable['I'] = 1, romanTable['V'] = 5, romanTable['X'] = 10;
         romanTable['L'] = 50, romanTable['C'] = 100, romanTable['D'] = 500;
         romanTable['M'] = 1000;
    };
};

int main(void) {
    Solution s;
    cout << s.romanToInt("XIV") << endl;
    cout << s.romanToInt("XVII") << endl;
    cout << s.romanToInt("LX") << endl;
    cout << s.romanToInt("CXCIX") << endl;
    cout << s.romanToInt("MMMCCCXXXIII") << endl;
    return 0;
};