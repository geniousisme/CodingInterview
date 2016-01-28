/*
The gray code is a binary numeral system
where two successive values differ in only one bit.
Given a non-negative integer n representing the total number of bits in the code,
print the sequence of gray code.
A gray code sequence must begin with 0.
For example, given n = 2, return [0,1,3,2]. Its gray code sequence is:

00 - 0
01 - 1
11 - 3
10 - 2

Note:
For a given n, a gray code sequence is not uniquely defined.
For example, [0,2,3,1] is also a valid gray code sequence
according to the above definition.
For now, the judge is able to judge based on one instance of gray code sequence.
Sorry about that.
*/

#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    vector<int> grayCode(int n) {
        int highestBit = 0;
        vector<int> res(1, 0);
        for(int i = 0; i < n; i++) {
            highestBit = pow(2, i);
            for (int k = res.size() - 1; k > -1; --k)
                 res.push_back(res[k] + highestBit);
        };
        return res;
    }
};

class Solution {
public:
    vector<int> grayCode(int n) {
        vector<int> res;
        int size = 1 << n;
        for(int i = 0; i < size; ++i)
            res.push_back((i >> 1) ^ i);
        return res;
    }
};

int main(void) {
    Solution s;
    Utils utils;
    utils.printIntVector(s.grayCode(2));
    return 0;
};