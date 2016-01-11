#include <iostream>

using namespace std;

class Solution1 { // use the power of two property to solve it.
public:
    int hammingWeight(uint32_t n) {
        int count = 0;
        while(n){
            count ++;
            n &= (n - 1);
        };
        return count;
    }
};

class Solution {
public:
    int hammingWeight(uint32_t n) {
        int count = 0;
        for (int i = 31; i > -1; --i) {
            count += (n & 1);
            n >>= 1;
        }
        return count;
    }
};

int main(int argc, char *argv []){
    Solution s;
    cout << "count: " << s.hammingWeight(9) << endl;
    cout << "count: " << s.hammingWeight(7) << endl;
    return 0;
};