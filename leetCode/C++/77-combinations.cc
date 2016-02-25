#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    vector<vector<int>> combine(int n, int k) {
        vector<int> comb;
        combine_helper(n, 1, k, comb);
        return res;
    }
private:
    vector<vector<int>> res;
    void combine_helper(int n, int start, int k, vector<int>& comb) {
        if (k == 0) {
            res.push_back(comb);
            return;
        }
        for (int i = start; i < n + k; ++i) {
            comb.push_back(i);
            /*
                since start + 1,
                let k - 1 to make the boundry(n + k - 1) of each starter be the same.
                Also, it will keep track if comb contains
                enough elements for the combination or not.
            */
            combine_helper(n, i + 1, k - 1, comb);
            comb.pop_back();
        }
    }
};

int main(void) {
    Solution s;
    vector<vector<int>> res;
    res = s.combine(4, 2);
    for (const auto &array: res) {
        for (const auto &elem: array)
            cout << elem << " ";
        cout << endl;
    }
    return 0;
};