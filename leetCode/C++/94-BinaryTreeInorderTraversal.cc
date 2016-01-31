/*
Given a binary tree,
return the inorder traversal of its nodes' values.

For example:
Given binary tree {1,#,2,3},
   1
    \
     2
    /
   3

return [1,3,2].
Note: Recursive solution is trivial, could you do it iteratively?
*/

#include <iostream>
#include <stack>
#include <vector>

using namespace std;

struct TreeNode {
     int val;
     TreeNode *left;
     TreeNode *right;
     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution1 {
public:
    vector<int> inorderTraversal(TreeNode* root) {
        inorder_traverse_helper(root);
        return res;
    }
private:
    vector<int> res;
    void inorder_traverse_helper(TreeNode* root) {
        if (root) {
            inorder_traverse_helper(root->left);
            res.push_back(root->val);
            inorder_traverse_helper(root->right);
        }
    }
};

class Solution {
public:
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> res;
        stack<TreeNode*> stk;
        while (!stk.empty() || root) {
            if (root) {
                stk.push(root);
                root = root->left;
            }
            else {
                TreeNode *top = stk.top();
                stk.pop();
                res.push_back(top->val);
                root = top->right;
            }
        }
        return res;
    }
};

int main(void){
    return 0;
}