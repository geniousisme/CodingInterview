#include <vector>
#include <iostream>

using namespace std;
/**
 * Definition for a binary tree node.
 */
struct TreeNode {
      int val;
      TreeNode *left;
      TreeNode *right;
      TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution1 { // DFS
public:
    vector<vector<int>> levelOrder(TreeNode* root) {
        vector<vector<int>> res;
        if (root)
            level_order_helper(root, res, 1);
        return res;
    }
private:
    void level_order_helper(TreeNode* root, vector<vector<int>>& res, int depth) {
        if (!root)
            return;
        if (depth > res.size()) {
            vector<int> new_level;
            res.push_back(new_level);
        }
        res[depth - 1].push_back(root->val);
        level_order_helper(root->left, res, depth + 1);
        level_order_helper(root->right, res, depth + 1);
    }
};

class Solution { // BFS
public:
    vector<vector<int>> levelOrder(TreeNode* root) {
        vector<vector<int>> res;
        vector<int> vals;
        vector<TreeNode*> curr_level;
        vector<TreeNode*> next_level;
        if (root) {
            curr_level.push_back(root);
            while (!curr_level.empty()) {
                TreeNode* top = curr_level.back();
                curr_level.pop_back();
                vals.push_back(top->val);
                if (top->left)
                    next_level.insert(next_level.begin(), top->left);
                if (top->right)
                    next_level.insert(next_level.begin(), top->right);
                if (curr_level.empty()) {
                    res.push_back(vals);
                    curr_level = next_level;
                    next_level.clear();
                    vals.clear();
                }
            }
        }
        return res;
    }
};

int main(void) {
    Solution s;
    TreeNode root(1);
    TreeNode lnode(2);
    TreeNode rnode(3);
    TreeNode llnode(4);
    TreeNode lrnode(5);
    TreeNode rlnode(6);
    TreeNode rrnode(7);
    (&root)->left = &lnode;
    (&root)->right = &rnode;
    (&root)->left->left = &llnode;
    (&root)->right->right = &rrnode;
    vector<vector<int>> level_orders = s.levelOrder(&root);
    for (const auto &level: level_orders) {
        cout << "[";
        for (const auto &node: level)
            cout << node << " ";
        cout << "]" << endl;
    }
    return 0;
};