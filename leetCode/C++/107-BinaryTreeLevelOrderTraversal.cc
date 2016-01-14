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
    vector<vector<int>> levelOrderBottom(TreeNode* root) {
        vector<vector<int>> res;
        
    }
private:
    vector<vector<int>> level_order_helper(TreeNode* root, int depth) {
        if (depth > res.size()) {
            vector<int> new_level {root->val};
            res.push_back(new_level);
        }
        else
            res[depth - 1].push_back(root->val);
        
    }
};