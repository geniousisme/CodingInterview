#include <iostream>

using namespace std;

class Solution {
public:
    double myPow(double x, int n) {
        bool negative_flag = false;
        if (n < 0) {
            negative_flag = true;
            n *= -1;
        }
        double res = 1, pow_sum = x;
        while (n) {
            if (n % 2)
                res *= pow_sum;
            pow_sum *= pow_sum;
            n /= 2;
        }
        if (negative_flag)
            return 1 / res;
        return res;
    }
};

int main(void) {
    Solution s;
    cout << s.myPow(34.00515, -3) << endl;
    return 0;
};