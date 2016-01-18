#include <iostream>
#include <limits>

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

class Solution {
public:
    int minDepth(TreeNode* root) {
        if (root)
            return min_depth_helper(root);
        return 0;
    }
private:
    int min_depth_helper(TreeNode* root) {
        if (!root)
            return numeric_limits<int>::max();
        if (!(root->left) && !(root->right))
            return 1;
        return min(min_depth_helper(root->left), min_depth_helper(root->right)) + 1;
    }
};

int main(void) {
    Solution s;
    TreeNode t1(1);
    TreeNode t2(2);
    (&t1)->left = &t2;
    cout << s.minDepth(&t1) << endl;
    return 0;
};