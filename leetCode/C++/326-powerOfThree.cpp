#include <cmath>

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

