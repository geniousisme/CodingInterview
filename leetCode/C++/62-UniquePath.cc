/*
A robot is located at the top-left corner of a m x n grid
(marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time.
The robot is trying to reach the bottom-right corner of the grid
(marked 'Finish' in the diagram below).

How many possible unique paths are there?
*/

#include <iostream>
#include <vector>

using namespace std;

class Solution1 {
public:
    int uniquePaths(int m, int n) {
        /*
            Time:  O(m * n)
            Space: O(m * n)
        */
        vector<vector<int>> maze(m, vector<int>(n, 0));
        for (int i = 0; i < m; ++i)
            maze[i][0] = 1;
        for (int j = 0; j < n; ++j)
            maze[0][j] = 1;
        for (int i = 1; i < m; ++i) {
            for (int j = 1; j < n; ++j)
                maze[i][j] = maze[i - 1][j] + maze[i][j - 1];
        }
        return maze[m - 1][n - 1];
    }
};

class Solution2 {
public:
    int uniquePaths(int m, int n) {
        /*
            Time:  O(m * n)
            Space: O(n)
        */
        vector<int> maze (n, 1);
        for (int i = 1; i < m; ++i) {
            for (int j = 1; j < n; ++j)
                maze[j] += maze[j - 1];
        }
        return maze[n - 1];
    }
};

class Solution {
public:
    int uniquePaths(int m, int n) {
        /*
            Time:  O(m + n)
            Space: O(1)
        */
        return factorial(m + n - 2) / (factorial(m - 1) * factorial(n - 1));
    }
private:
    double factorial(double n) {
        if (n <= 1)
            return 1;
        return n * factorial(n - 1);
    }
};


int main(void) {
    Solution s;
    cout << s.uniquePaths(36, 7) << endl;
    return 0;
};