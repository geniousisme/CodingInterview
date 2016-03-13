/*
Given a binary tree and a sum,
find all root-to-leaf paths where each path's sum equals the given sum.

For example:
Given the below binary tree and sum = 22,
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
return
[
   [5,4,11,2],
   [5,8,4,5]
]
*/

#include <iostream>
#include <vector>

using namespace std;

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    vector<vector<int>> pathSum(TreeNode* root, int sum) {
        /*
            Time:  O(n)
            Space: O(logn)
        */
        if (root) {
            vector<int> candidates;
            path_sum_helper(root, candidates, 0, sum);
        }
        return res;
    }
private:
    vector<vector<int>> res;
    void path_sum_helper(TreeNode* root, vector<int> candidates, int curr_sum, int target_sum) {
        if (!root)
            return;
        if (!(root->left) && !(root->right) && curr_sum + root->val == target_sum) {
            candidates.push_back(root->val);
            res.push_back(candidates);
            candidates.pop_back();
            return;
        }
        candidates.push_back(root->val);
        path_sum_helper(root->left, candidates, curr_sum + root->val, target_sum);
        path_sum_helper(root->right, candidates, curr_sum + root->val, target_sum);
        candidates.pop_back();
    }
};