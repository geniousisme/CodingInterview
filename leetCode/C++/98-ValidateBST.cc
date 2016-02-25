/*

Given a binary tree,
determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

*/

#include <iostream>
#include <stack>
#include <vector>

using namespace std;

/*
    Definition for a binary tree node.
*/

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution1 { // recursive solution
public:
    bool isValidBST(TreeNode* root) {
        /*
            Time:  O(n)
            Space: O(n)
        */
        if (root) {
            double inf = numeric_limits<double>::infinity();
            return validate_bst_helper(root, inf, -inf);
        }
        return true;
    }
private:
    bool validate_bst_helper(TreeNode* root, double upper_bound, double lower_bound) {
        if (!root)
            return true;
        if (root->val >= upper_bound || root->val <= lower_bound)
            return false;
        return validate_bst_helper(root->left, root->val, lower_bound) && validate_bst_helper(root->right, upper_bound, root->val);
    }
};

class Solution { // iterative soltion
public:
    bool isValidBST(TreeNode* root) {
        /*
            Time:  O(n)
            Space: O(n)
        */
        if (!root)
            return true;
        stack<TreeNode*> stk;
        TreeNode* top, *prev = nullptr;
        while (!stk.empty() || root) {
            if (root) {
                stk.push(root);
                root = root->left;
            }
            else {
                top = stk.top();
                stk.pop();
                if (prev && prev->val >= top->val)
                    return false;
                prev = top;
                root = top->right;
            }
        }
        return true;
    }
};

int main(void) {
    Solution s;
    TreeNode root(0);
    cout << s.isValidBST(&root) << endl;
    return 0;
};