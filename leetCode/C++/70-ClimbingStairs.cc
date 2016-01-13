#include <iostream>
#include <vector>

using namespace std;

class Solution1 { // recursive solution
public:
    int climbStairs(int n) {
        /*
            Time:  O(n)
            Space: O(n)
        */
        if (n <= 1)
            return 1;
        return climbStairs(n - 1) + climbStairs(n - 2);
    }
};

class Solution2 { // iterative solution
public:
    int climbStairs(int n) {
        /*
            Time:  O(n)
            Space: O(n)
        */
        vector<int> lookup {1, 1};
        if (n <= 1)
            return lookup[n];
        for (int i = 2; i < n + 1; ++i)
            lookup.push_back(lookup[i - 1] + lookup[i - 2]);
        return lookup[n];
    }
};

class Solution { // iterative solution with constant space
public:
    int climbStairs(int n) {
        /*
            Time:  O(n)
            Space: O(1)
        */
        int prev = 1, prev_prev = 1, res = 0;
        if (n <= 1)
            return 1;
        for (int i = 2; i < n + 1; ++i) {
            res = prev + prev_prev;
            prev_prev = prev;
            prev = res;
        }
        return res;
    }
};


int main(void) {
    Solution s;
    for (int i = 0; i < 45; i++)
        cout << s.climbStairs(i) << " ";
    cout << endl;
    return 0;
};

// 1 2 3 4
// 1 2 3 5