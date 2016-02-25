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
    bool isSymmetric(TreeNode* root) {
        return is_symmetric_helper(root, root);
    }
private:
    bool is_symmetric_helper(TreeNode* left_root, TreeNode* right_root) {
        if (!left_root && !right_root)
            return true;
        else if (left_root && right_root && left_root->val == right_root->val)
            return is_symmetric_helper(left_root->right, right_root->left) && is_symmetric_helper(left_root->left, right_root->right);
        else
            return false;
    }
};