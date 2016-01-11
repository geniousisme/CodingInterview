#include <iostream>

using namespace std;

class Solution {
public:
    int trailingZeroes(int n) {
        int five_count = 0;
        while (n >= 5) {
            five_count += n / 5;
            n /= 5;
        }
        return five_count;
    }
};

int main(void) {
    Solution s;
    cout << s.trailingZeroes(4) << endl;
};