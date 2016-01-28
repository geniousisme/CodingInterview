#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        if (!nums.empty()) {
            vector<int> sub;
            sort(nums.begin(), nums.end());
            subset_helper(nums, sub, 0);
        }
        return res;
    }
private:
    vector<vector<int>> res;
    void subset_helper(vector<int>& nums, vector<int>& sub, int start_pos) {
        res.push_back(sub);
        for (int i = start_pos; i < nums.size(); ++i) {
            sub.push_back(nums[i]);
            subset_helper(nums, sub, i + 1);
            sub.pop_back();
        }
        return;
    }
};

int main(void) {
    Solution s;
    vector<int> test {1, 2, 3};
    vector<vector<int>> res = s.subsets(test);
    for (const auto &sub: res) {
        cout << "[ ";
        for (const auto &num: sub)
            cout << num << " ";
        cout << "]" << endl;
    }
    return 0;
};