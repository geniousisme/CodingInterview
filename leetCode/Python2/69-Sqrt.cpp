#include <cmath>
#include <iostream>
using namespace std;

class Solution {
public:
    int mySqrt(int x) {
        if (x < 2)
            return x;
        float last_res = 1, curr_res = x;
        while (abs(curr_res - last_res) > 0.1) {
            last_res = curr_res;
            curr_res = 0.5 * (last_res + x / last_res);
            cout << "last_res: " << last_res << endl;
            cout << "curr_res: " << curr_res << endl;
        }
        return curr_res + 0.5;
    }
};

int main(void) {
    Solution s;
    s.mySqrt(2147395599);
    return 0;
};