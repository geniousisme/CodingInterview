#include <cmath>
#include <iostream>

using namespace std;

class Solution1 { // log calculation
public:
    bool isPowerOfThree(int n) {
        if (n < 1)
            return false;
        return n == pow(3, round((log(n) / log(3))));
    }
};

class Solution2 { // iterative
public:
    bool isPowerOfThree(int n) {
        if (n < 1)
            return false;
        while (n > 1) {
            if (n % 3 != 0)
                return false;
            n /= 3;
        }
        return true;
    }
};

class Solution { // recursive
public:
    bool isPowerOfThree(int n) {
        if (n <= 0)
            return false;
        if (n == 1)
            return true;
        return n % 3 == 0 && isPowerOfThree(n / 3);
    }
};

int main(void) {
    Solution s;
    cout << "243: " << s.isPowerOfThree(243) << endl;
    cout << "6: " << s.isPowerOfThree(6) << endl;
    cout << "1: " << s.isPowerOfThree(1) << endl;
    cout << "0: " << s.isPowerOfThree(0) << endl;
    return 0;
}
