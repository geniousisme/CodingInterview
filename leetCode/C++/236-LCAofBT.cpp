#include <iostream>

using namespace std;

/**
 * Definition for a binary tree node.
 **/
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        if (!root)
            return root;
        if (root == p or root == q)
            return root;

        TreeNode* left_lca = lowestCommonAncestor(root->left, p, q);
        TreeNode* right_lca = lowestCommonAncestor(root->right, p, q);

        if (left_lca && right_lca)
            return root;

        return left_lca ? left_lca : right_lca;
    }
};

int main(void) {
    Solution s;
    TreeNode root(1);
    TreeNode lnode(2);
    TreeNode rnode(3);
    TreeNode llnode(4);
    TreeNode rrnode(5);
    (&root)->left = &lnode;
    (&root)->right = &rnode;
    (&root)->left->left = &llnode;
    (&root)->right->right = &rrnode;
    cout << s.lowestCommonAncestor(&root, (&root)->left, (&root)->right->right)->val << endl;
    cout << s.lowestCommonAncestor(&root, (&root)->left, (&root)->right)->val << endl;
    cout << s.lowestCommonAncestor(&root, (&root)->left, (&root)->left->left)->val << endl;

    return 0;
};