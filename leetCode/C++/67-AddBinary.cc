/*
Given two binary strings, return their sum (also a binary string).

For example,
a = "11"
b = "1"
Return "100".
*/

#include <iostream>
#include <string>
#include <vector>

using namespace std;

class Solution {
public:
    string addBinary(string a, string b) {
        string::reverse_iterator ait = a.rbegin(), bit = b.rbegin();
        vector<int> units;
        while (ait != a.rend() || bit != b.rend()) {
            int unit = 0;
            if (ait != a.rend()) {
                unit += (*ait) - '0';
                ++ait;
            }
            if (bit != b.rend()) {
                unit += (*bit) - '0';
                ++bit;
            }
            units.push_back(unit);
        }
        string binary_res = "";
        int carry = 0;
        for (auto &unit: units) {
            unit += carry;
            binary_res = to_string(unit % 2) + binary_res;
            carry = unit / 2;
        }
        if (carry)
            binary_res = to_string(carry) + binary_res;
        return binary_res;
    }
};

int main(void) {
    Solution s;
    cout << s.addBinary("11", "1") << endl;
    return 0;
};