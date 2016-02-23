#include <iostream>

using namespace std;

class Solution {
public:
    bool isUgly(int num) {
        if (num < 1)
            return false;
        int ugly_nums[] = {2, 3, 5};
        for (const auto &ugly_num: ugly_nums) {
            while (num % ugly_num == 0)
                num /= ugly_num;
        }
        return num == 1;
    }
};

int main(void) {
    Solution s;
    cout << s.isUgly(1) << endl;
    cout << s.isUgly(6) << endl;
    cout << s.isUgly(8) << endl;
    cout << s.isUgly(120) << endl;
    cout << s.isUgly(14) << endl;
    cout << s.isUgly(13) << endl;
    return 0;
};
