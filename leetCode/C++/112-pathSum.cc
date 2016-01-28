/*

Given a binary tree and a sum, determine
if the tree has a root-to-leaf path
such that adding up all the values along the path equals the given sum.

For example:
Given the below binary tree and sum = 22,
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \      \
        7    2      1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
*/

/**
 * Definition for a binary tree node.
*/
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
public:
    bool hasPathSum(TreeNode* root, int sum) {
        if (!root)
            return false;
        return path_sum_helper(root, 0, sum);
    }
private:
    bool path_sum_helper(TreeNode* root, int curr_sum, int target_sum) {
        if (!root)
            return false;
        curr_sum += root->val;
        if (!(root->left) && !(root->right))
            return curr_sum == target_sum;
        else
            return (path_sum_helper(root->left, curr_sum, target_sum)
                    || path_sum_helper(root->right, curr_sum, target_sum));
    }
};