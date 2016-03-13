/*
You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Follow up:
Could you do this in-place?
*/

#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        /*
            Time:  O(m * n)
            Space: O(1)
        */
        for (int i = 0; i < matrix.size(); ++i) {
            for (int j = i + 1; j < matrix[0].size(); ++j)
                swap(matrix, i, j);
        }
        for (int i = 0; i < matrix.size(); ++i)
            reverse(matrix[i].begin(), matrix[i].end());
    }
private:
    void swap(vector<vector<int>>& matrix, int x, int y) {
        int tmp = matrix[x][y];
        matrix[x][y] = matrix[y][x];
        matrix[y][x] = tmp;
    }
};

int main(void) {
    Solution s;
    vector<vector<int>> matrix {{1, 2, 3},
                                {4, 5, 6},
                                {7, 8, 9}};
    s.rotate(matrix);
    for (const auto &row: matrix){
        for (const auto &num: row)
            cout << num << " ";
        cout << endl;
    }
    return 0;

};