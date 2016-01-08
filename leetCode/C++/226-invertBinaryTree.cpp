#include <iostream>
#include <vector>
#include <queue>

using namespace std;

struct TreeNode {
       int val;
       TreeNode *left;
       TreeNode *right;
       TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
public:
    TreeNode* invertTree(TreeNode* root) {
        if (!root)
          return root;

        TreeNode* rootleft = root->left;
        root->left = invertTree(root->right);
        root->right = invertTree(rootleft);

        return root;
    }
};

class Solution {
public:
    TreeNode* invertTree(TreeNode* root) {
        if (!root)
            return root;

        TreeNode* rootleft = root->left;
        root->left = root->right;
        root->right = rootleft;

        invertTree(root->left);
        invertTree(root->right);

        return root;
    }
};

class Solution {
public:
    TreeNode* invertTree(TreeNode* root) { // iteratively invert the tree.
        TreeNode *new_root = root;
        if (root) {
          queue<TreeNode*> queue;
          queue.push(root);
          while (!queue.empty()) {
                 root = queue.front();
                 queue.pop();
                 TreeNode *rootleft = root->left;
                 root->left = root->right;
                 root->right = rootleft;
                 if (root->left)
                     queue.push(root->left);
                 if (root->right)
                     queue.push(root->right);
          };
        };
        return new_root;
    }
};