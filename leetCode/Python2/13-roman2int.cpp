#include <string>
#include <vector>

class Solution {
public:
    int romanToInt(string s) {
        init();
        int res = 0;
        for (int i = 0; i < s.length() - 1; i++) {
            if (romanTable[s[i]] < romanTable[s[i + 1]])
                res -= romanTable[s[i]];
            else
                res += romanTable[s[i]];
        }
        res += romanTable[s[i]];
        return res;
    }
private:
    int romanTable[255];
    void init(void) {
        romanTable['I'] = 1, romanTable['V'] = 5, romanTable['X'] = 10;
        romanTable['L'] = 50, romanTable['C'] = 100, romanTable['D'] = 500;
        romanTable['M'] = 1000;
    };
};