#include <iostream>
#include <queue>
#include <string>
#include <vector>

using namespace std;

/*
 * Definition for a binary tree node.
 */

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

struct NodeAndPath {
    TreeNode* node;
    string path;
    NodeAndPath(TreeNode* root, string path) : node(root), path(path) {}
};


class Solution1 { // recursive
public:
    vector<string> binaryTreePaths(TreeNode* root) {
        vector<string> res;
        if (root)
            binary_path_helper(root, to_string(root->val), res);
        return res;
    }
private:
    void binary_path_helper(TreeNode* root, string path, vector<string>& res) {
        if (!(root->left) && !(root->right)) {
            res.push_back(path);
            return;
        }
        if (root->left)
            binary_path_helper(root->left, path + "->" + to_string(root->left->val), res);
        if (root->right)
            binary_path_helper(root->right, path + "->" + to_string(root->right->val), res);
    }
};

class Solution { // iterative
public:
    vector<string> binaryTreePaths(TreeNode* root) {
        queue<NodeAndPath*> node_queue;
        vector<string> res;
        if (!root)
            return res;
        NodeAndPath root_and_path(root, to_string(root->val));
        node_queue.push(&root_and_path);
        while (!node_queue.empty()) {
            NodeAndPath *root_and_path = node_queue.front();
            TreeNode* root = root_and_path->node;
            string path = root_and_path->path;
            node_queue.pop();
            if (!(root->left) && !(root->right))
                res.push_back(path);
            if (root->left) {
                NodeAndPath left_and_path(root->left, path + "->" + to_string(root->left->val));
                node_queue.push(&left_and_path);
            }
            if (root->right) {
                NodeAndPath right_and_path(root->right, path + "->" + to_string(root->right->val));
                node_queue.push(&right_and_path);
            }
        }
        return res;
    }
};

int main(void) {
    Solution s;
    TreeNode t1(1);
    TreeNode t2(2);
    TreeNode t3(3);
    TreeNode t4(4);
    TreeNode t5(5);
    (&t1)->left = &t2;
    (&t1)->right = &t3;
    (&t3)->right = &t4;
    (&t3)->left = &t5;
    vector<string> res = s.binaryTreePaths(&t1);
    for (const auto &path: res)
        cout << path << " ";
    cout << endl;
    return 0;
};