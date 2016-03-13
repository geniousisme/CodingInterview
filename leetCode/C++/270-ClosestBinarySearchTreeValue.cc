#include <cmath>
#include <iostream>
#include <limits>
#include <vector>

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
    int closestValue(TreeNode* root, double target) {
        double closet_candidate = 0;
        double min_diff = numeric_limits<double>::max();
        while (root) {
            double diff = abs(root->val - target);
            if (diff < min_diff) {
                closet_candidate = root->val;
                min_diff = diff;
            }
            if (root->val > target)
                root = root->left;
            else if (root->val < target)
                root = root->right;
            else
                return root->val;
        }
        return closet_candidate;
    }
};

int main(void) {
    Solution s;
    // TreeNode t4(4);
    TreeNode t1(1);
    // TreeNode t9(9);
    // (&t4)->left = &t1;
    // (&t4)->right = &t9;

    cout << s.closestValue(&t1, 4.28541) << endl;
    // cout << s.closestValue(&t4, 5) << endl;
    // cout << s.closestValue(&t4, 10) << endl;

    return 0;
};