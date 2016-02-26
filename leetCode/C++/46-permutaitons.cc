#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int>> res;
        if (!nums.empty()) {
            total_length = nums.size();
            vector<int> perm;
            vector<bool> visited(total_length, false);
            permute_helper(nums, perm, res, visited);
        }
        return res;
    }
private:
    int total_length = 0;
    void permute_helper(vector<int>& nums, vector<int>& perm, vector<vector<int>>& res, vector<bool>& visited) {
        if (perm.size() == total_length) {
            res.push_back(perm);
            return;
        }
        for (int i = 0; i < nums.size(); ++i) {
            if (!visited[i]) {
                visited[i] = true;
                perm.push_back(nums[i]);
                permute_helper(nums, perm, res, visited);
                perm.pop_back();
                visited[i] = false;
            }
        }
    }
};

// class Solution {
// public:
//     vector<vector<int> > permute(vector<int>& nums) {
//                          vector<vector<int> > res;
//                          if (!nums.empty()) {
//                              vector<int> perm, visited(nums.size(), 0);
//                              permuteHelper(res, visited, nums, perm, nums.size());
//                          };
//                          return res;
//     }
// private:
//     void permuteHelper(vector<vector<int> >& res, vector<int>& visited, vector<int>& nums, vector<int>& perm, int totalLen) {
//          if (perm.size() == totalLen) {
//              res.push_back(perm);
//              return;
//          };
//          for (int i = 0; i < nums.size(); i++) {
//               if (visited[i] == 0) {
//                   perm.push_back(nums[i]);
//                   visited[i] = 1;
//                   permuteHelper(res, visited, nums, perm, totalLen);
//                   visited[i] = 0;
//                   perm.pop_back();
//               };
//          };
//     }; 
// };

int main(void) {
    Solution s;
    Utils u;
    int iarr [] = {1, 2, 3};
    vector<int> nums(iarr, iarr + sizeof(iarr) / sizeof(iarr[0]));
    u.print2DIntVector(s.permute(nums));
    return 0;
}